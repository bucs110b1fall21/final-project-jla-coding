import sys
import pygame
import random
import math
import json
from src import player
from src import economy
from src import wall
from src import prop
from src import interactable
from src.inventory import Inventory,InventorySlot,EquipableSlot,InventoryItem,Consumable,Equipable

class Controller:
    def __init__(self, width=800, height=600):
        pygame.init()
        
        #self.debug_mode = False #change this to turn debug mode on and off. Feel free to add or remove stuff from debug mode
        self.myfont = pygame.font.SysFont('Calibri', 22)
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        #self.background.fill((100, 100, 100))
        self.background = pygame.Surface(self.screen.get_size()).convert()
        self.background = pygame.image.load("assets/EMPTY ROOM.png")
        pygame.font.init()  
        pygame.key.set_repeat(1, 25)  #this may not actually be needed       
        self.player = player.Player(self)
        
        level_data_ptr = open("src/level_data.json",'r')
        self.level_data = json.load(level_data_ptr) #saves dictionary of levels and their data
        level_data_ptr.close()
        
        self.props = pygame.sprite.Group()
        self.walls = []
        self.interactables = pygame.sprite.Group() #group of interacts in scene
        self.all_sprites = pygame.sprite.Group((self.player,) + tuple(self.props) + tuple(self.interactables))
        self.load_level("wall_test")
        self.state = "GAME"

        #self.debug_props = pygame.sprite.Group()       
        #if self.debug_mode: #add debug sprites here
            #self.debug_interact_x = prop.Prop("assets/black_pixel.png", self.player.rect.center[0] - self.player.reach, self.player.rect.center[1], self.player.reach*2, 1) #sprite showing interaction zone in x direction
            #self.debug_interact_y = prop.Prop("assets/black_pixel.png", self.player.rect.center[0], self.player.rect.center[1] - self.player.reach, 1, self.player.reach*2) #sprite showing interaction zone in x direction
            #self.debug_props.add(self.debug_interact_x) #add debug sprites
            #self.debug_props.add(self.debug_interact_y)    
        #self.all_sprites = pygame.sprite.Group((self.player,) + tuple(self.props) + tuple(self.interactables) + tuple(self.debug_props)) #group of all sprites in scene

        self.load_level("interactable_test") #load test level
        self.state = "GAME" #set game to run
    
    def load_level(self, level_name):
        '''
            Loads the specified level from level_data
            args: self, level_name (string)
            returns: None
        '''
        data = self.level_data[level_name] #data = relevent level data
        for prop_data in data["props"]: #for props in prop list, add the prop
            self.props.add(prop.Prop(prop_data[0], prop_data[1], prop_data[2], prop_data[3], prop_data[4]))
        for wall_data in data["walls"]: #for walls in wall list, add the wall
            self.walls.append(wall.Wall(wall_data[0], wall_data[1], wall_data[2], wall_data[3]))
        for interactable_data in data["interactables"]: #for interactables in interactable list, and the interactable
            self.interactables.add(interactable.Interactable(interactable_data[0], interactable_data[1], interactable_data[2], interactable_data[3], interactable_data[4], interactable_data[5]))
        player_data = data["player_data"]
        self.player.goto(player_data[0], player_data[1])
        self.player.face(player_data[2])
        self.all_sprites = pygame.sprite.Group((self.player,) + tuple(self.props) + tuple(self.interactables))
        self.inventory = Inventory(self.player,5,5,1)
        self.player.goto(player_data[0], player_data[1]) #move player to correct spot
        self.player.face(player_data[2]) #turn player in correct direction
        #self.all_sprites = pygame.sprite.Group((self.player,) + tuple(self.props) + tuple(self.interactables) + tuple(self.debug_props)) #set all sprites to the new sprite groups (may not be nescesary?)
        food = Consumable('assets/Chickenbag.png', 1, 10, 0)
        food2 = Consumable('assets/WacDonaldsBag.png', 1, 10, 0)
        beverage = Consumable('assets/WonsterEnergy.png', 1, 0, 10)
        beverage2 = Consumable('assets/RedbullCan.png', 1, 0, 10)
        self.inventory.addItemInv(food)
        self.inventory.addItemInv(food2)
        self.inventory.addItemInv(beverage)
        self.inventory.addItemInv(beverage2)
    
    def unload_level(self):
        '''
            Unloads the level
            args: self
            returns: None
        '''
        for prop in self.props: #kill all props
            prop.kill()
        while walls: #remove all walls
            walls[0].pop()
        for interactable in interactables: #kill all interactables
            interactable.kill()
    
    
    def mainLoop(self):
        '''
            Main game loop
            args: self
            returns: None
        '''
        while True:
            if(self.state == "GAME"):
                self.gameLoop()
            elif(self.state == "GAMEOVER"):
                self.gameOver()
    
    
    def handle_interactions(self, interactions):
        '''
            Handles interactions for objects and what they do based on their ID
            args: self, list [String]
            returns: None
        '''
        for i in interactions:
            if i == 'computer':
                print('interacted with computer')
            elif i == 'sink':
                self.player.drink(30)
            else:
                raise ValueError

    def draw_player_stats(self):
        
        self.hunger = self.myfont.render(f"{int(self.player.hunger)}", False, (250,250,250))
        self.thirst = self.myfont.render(f"{int(self.player.thirst)}" , False, (250,250,250))
        self.money = self.myfont.render(f"{self.player.money}" , False, (250,250,250))
        self.coins = self.myfont.render(f"{self.player.crypto}" , False, (250,250,250))
        self.hungerimg = pygame.image.load('assets/BurgerIcon.png').convert_alpha()
        self.thirstimg = pygame.image.load('assets/WaterIcon.png').convert_alpha()
        self.moneyimg = pygame.image.load('assets/dollar.png').convert_alpha()
        self.coinimg = pygame.image.load('assets/coin.png').convert_alpha()
        self.screen.blit(self.hunger,(50,8))
        self.screen.blit(self.thirst,(50,58))
        self.screen.blit(self.money,(50,108))
        self.screen.blit(self.coins,(50,158))
        self.screen.blit(self.hungerimg,(20,10))
        self.screen.blit(self.thirstimg,(20,60))
        self.screen.blit(self.moneyimg,(20,110))
        self.screen.blit(self.coinimg,(20,160)) 
        
    def gameLoop(self):
        '''
            Game loop
            args: self
            returns: None
        '''
    
        loop_time = pygame.time.Clock() #keeps track of time since last frame
        prev_key_state = {
            "e": pygame.key.get_pressed()[pygame.K_e],
            "v": pygame.key.get_pressed()[pygame.K_v]
            } #last press state of key
        loop_time.tick() #sets the time to 0
        while self.state == "GAME":
            dt = loop_time.tick(60) #records dt, the time the last frame took in milliseconds and caps framerate at 60fps
            if(dt > 20): #if lag occurs, print
                print("lag detected")
            if self.player.hunger <= 0 or self.player.thirst <= 0:
                self.state = "GAMEOVER"
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            #if key presses are an event it has trouble updating when a key stops being pressed
            pressed = pygame.key.get_pressed() #allows multiple buttons to be active
            if pressed[pygame.K_w]:
                self.player.move('U', self.walls, dt)
            if pressed[pygame.K_s]:
                self.player.move('D', self.walls, dt)
            if pressed[pygame.K_a]:
                self.player.move('L', self.walls, dt)
            if pressed[pygame.K_d]:
                self.player.move('R', self.walls, dt)
            if pressed[pygame.K_v] and not prev_key_state["v"]:
                self.inventory.toggleInventory()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                if self.inventory.display_inventory:
                    mouse_pos = pygame.mouse.get_pos()
                    self.inventory.checkSlot(self.screen, mouse_pos)
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if self.inventory.display_inventory:
                    self.inventory.moveItem(self.screen)
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                if self.inventory.display_inventory:
                    self.inventory.placeItem(self.screen)
            if pressed[pygame.K_e] and not prev_key_state["e"]: #interacts with objects (will not work if e was pressed last frame)
                interactions = []
                for interact in self.interactables: #create list of interactions this frame
                    interaction = interact.attempt_interact(self.player)
                    if interaction:
                        interactions.append(interaction) #add interaction if interaction is not None
                self.handle_interactions(interactions) #handle interactions
            prev_key_state["e"] = pressed[pygame.K_e]
            prev_key_state["v"] = pressed[pygame.K_v]
            if pressed[pygame.K_i]: #for testing (i stands for info, add whatever needs testing)
                print(self.player.hunger, self.player.thirst, self.player.direction)

            # redraw the entire screen
            #if self.debug_mode:
                #self.debug_interact_x.goto(self.player.rect.center[0] - self.player.reach, self.player.rect.center[1])
                #self.debug_interact_y.goto(self.player.rect.center[0], self.player.rect.center[1] - self.player.reach)
            self.all_sprites.update()
            #self.player.update_wealth()
            self.player.update_health(dt) #update player hunger and thirst
            #self.screen.blit(self.background, (0, 0))
            self.screen.blit(pygame.transform.scale(self.background, (self.width,self.height)), (0, 0))

            if self.player.hunger == 0 or self.player.thirst == 0:
                self.state = "GAMEOVER"

            self.draw_player_stats()
            self.all_sprites.draw(self.screen) #draw sprites
            self.inventory.draw(self.screen)
            pygame.display.flip() # update the screen

        
    def gameOver(self):
        '''
            Handles gameover state
            args: self
            returns: None
        '''
        self.background.fill((255, 0, 0))
        self.screen.blit(self.background, (0, 0))
        myfont = pygame.font.SysFont(None, 40)
        message = myfont.render('Game Over', False, (0, 0, 0))
        self.screen.blit(message, (self.width / 3, self.height / 3))
        pygame.display.flip()
        while True:
            for event in pygame.event.get(): #make sure you can quit in gameover
                if event.type == pygame.QUIT:
                    sys.exit()

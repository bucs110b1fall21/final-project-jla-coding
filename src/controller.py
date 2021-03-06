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
from src import computer
from src import button
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
        self.background.fill((100, 100, 100))
        pygame.font.init()  
        pygame.key.set_repeat(1, 25)  #this may not actually be needed       
        self.player = player.Player(self)
        self.economy = economy.Economy()
        self.computer_screen = computer.ComputerScreen(self)
        self.inventory = Inventory(self.player,5,5,1)
        
        level_data_ptr = open("src/level_data.json",'r')
        self.level_data = json.load(level_data_ptr) #saves dictionary of levels and their data
        level_data_ptr.close()
        
        self.props = pygame.sprite.Group()
        self.walls = []
        self.interactables = pygame.sprite.Group() #group of interacts in scene
        self.all_sprites = pygame.sprite.Group(tuple(self.props) + tuple(self.interactables) + (self.player,))

        #self.debug_props = pygame.sprite.Group()       
        #if self.debug_mode: #add debug sprites here
            #self.debug_interact_x = prop.Prop("assets/black_pixel.png", self.player.rect.center[0] - self.player.reach, self.player.rect.center[1], self.player.reach*2, 1) #sprite showing interaction zone in x direction
            #self.debug_interact_y = prop.Prop("assets/black_pixel.png", self.player.rect.center[0], self.player.rect.center[1] - self.player.reach, 1, self.player.reach*2) #sprite showing interaction zone in x direction
            #self.debug_props.add(self.debug_interact_x) #add debug sprites
            #self.debug_props.add(self.debug_interact_y)    
        #self.all_sprites = pygame.sprite.Group((self.player,) + tuple(self.props) + tuple(self.interactables) + tuple(self.debug_props)) #group of all sprites in scene

        self.load_level("game_level") #load test level
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
        self.all_sprites = pygame.sprite.Group(tuple(self.props) + tuple(self.interactables) + (self.player,))
        self.player.goto(player_data[0], player_data[1]) #move player to correct spot
        self.player.face(player_data[2]) #turn player in correct direction
        #self.all_sprites = pygame.sprite.Group((self.player,) + tuple(self.props) + tuple(self.interactables) + tuple(self.debug_props)) #set all sprites to the new sprite groups (may not be nescesary?)
        beverage = Consumable('assets/WonsterEnergy.png', 1, 0, 10)
        beverage2 = Consumable('assets/RedbullCan.png', 1, 0, 10)
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
                self.computer_screen.toggle_display()
            elif i == 'sink':
                self.player.drink(30)
            else:
                raise ValueError

    def draw_player_stats(self):
        
        self.hunger = self.myfont.render(f"{int(self.player.hunger)}", False, (250,250,250))
        self.thirst = self.myfont.render(f"{int(self.player.thirst)}" , False, (250,250,250))
        self.money = self.myfont.render(f"{int(self.player.money)/100}" , False, (250,250,250))
        self.coins = self.myfont.render(f"{int(1000*self.player.crypto)/1000}" , False, (250,250,250))
        self.hungerimg = pygame.image.load('assets/BurgerIcon.png').convert_alpha()
        self.thirstimg = pygame.image.load('assets/WaterIcon.png').convert_alpha()
        self.moneyimg = pygame.image.load('assets/dollar.png').convert_alpha()
        self.coinimg = pygame.image.load('assets/coin.png').convert_alpha()
        self.screen.blit(self.hunger,(50,30))
        self.screen.blit(self.thirst,(50,60))
        self.screen.blit(self.money,(50,90))
        self.screen.blit(self.coins,(50,120))
        self.screen.blit(self.hungerimg,(20,30))
        self.screen.blit(self.thirstimg,(20,60))
        self.screen.blit(self.moneyimg,(20,90))
        self.screen.blit(self.coinimg,(20,120)) 
        
    def gameLoop(self):
        '''
            Game loop
            args: self
            returns: None
        '''
    
        loop_time = pygame.time.Clock() #keeps track of time since last frame
        prev_key_state = {
            "e": pygame.key.get_pressed()[pygame.K_e],
            "u": pygame.key.get_pressed()[pygame.K_u],
            "v": pygame.key.get_pressed()[pygame.K_v],
            "left": pygame.key.get_pressed()[pygame.K_LEFT],
            "right": pygame.key.get_pressed()[pygame.K_RIGHT],
            "down": pygame.key.get_pressed()[pygame.K_DOWN],
            "up": pygame.key.get_pressed()[pygame.K_UP],
            "return": pygame.key.get_pressed()[pygame.K_RETURN],
            "space": pygame.key.get_pressed()[pygame.K_SPACE]
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
            if pressed[pygame.K_u] and not prev_key_state["u"]:
                food = Consumable('assets/Chickenbag.png', 1, 10, 0)
                food2 = Consumable('assets/WacDonaldsBag.png', 1, 10, 0)
                chance = 0
                chance += random.randrange(1,3)
                self.player.money -= 2000
                if chance == 1:
                    self.inventory.addItemInv(food)
                elif chance == 2:
                    self.inventory.addItemInv(food2)
            if pressed[pygame.K_UP]:
                if self.computer_screen.display_screen:
                    self.computer_screen.increase_button.select()
                    if not prev_key_state["up"]:
                        self.computer_screen.increase_percentage()
            if pressed[pygame.K_DOWN]:
                if self.computer_screen.display_screen:
                    self.computer_screen.decrease_button.select()
                    if not prev_key_state["down"]:
                        self.computer_screen.decrease_percentage()
            if pressed[pygame.K_LEFT] and not prev_key_state["left"]:
                if self.computer_screen.display_screen:
                    self.computer_screen.sell_button.deselect()
                    self.computer_screen.buy_button.select()
            if pressed[pygame.K_RIGHT] and not prev_key_state["right"]:
                if self.computer_screen.display_screen:
                    self.computer_screen.buy_button.deselect()
                    self.computer_screen.sell_button.select()
            if (pressed[pygame.K_RETURN] and not prev_key_state["return"]) or (pressed[pygame.K_SPACE] and not prev_key_state["space"]):
                if self.computer_screen.buttons[2].selected: #buy button
                    self.computer_screen.buy()
                elif self.computer_screen.buttons[3].selected: #sell button
                    self.computer_screen.sell()
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
                if self.computer_screen.display_screen:
                    self.computer_screen.toggle_display()
                else:
                    interactions = []
                    for interact in self.interactables: #create list of interactions this frame
                        interaction = interact.attempt_interact(self.player)
                        if interaction:
                            interactions.append(interaction) #add interaction if interaction is not None
                    self.handle_interactions(interactions) #handle interactions
            if not pressed[pygame.K_DOWN]:
                self.computer_screen.decrease_button.deselect()
            if not pressed[pygame.K_UP]:
                self.computer_screen.increase_button.deselect()
            prev_key_state["e"] = pressed[pygame.K_e]
            prev_key_state["u"] = pressed[pygame.K_u]
            prev_key_state["v"] = pressed[pygame.K_v]
            prev_key_state["left"] = pressed[pygame.K_LEFT]
            prev_key_state["right"] = pressed[pygame.K_RIGHT]
            prev_key_state["up"] = pressed[pygame.K_UP]
            prev_key_state["down"] = pressed[pygame.K_DOWN]
            prev_key_state["return"] = pressed[pygame.K_RETURN]
            prev_key_state["space"] = pressed[pygame.K_SPACE]
            if pressed[pygame.K_i]: #for testing (i stands for info, add whatever needs testing)
                print(self.computer_screen.decrease_button.selected)

            # redraw the entire screen
            #if self.debug_mode:
                #self.debug_interact_x.goto(self.player.rect.center[0] - self.player.reach, self.player.rect.center[1])
                #self.debug_interact_y.goto(self.player.rect.center[0], self.player.rect.center[1] - self.player.reach)
            self.all_sprites.update()

            self.player.update_health(dt) #update player hunger and thirst

            self.economy.changerate(dt)
            self.player.update_health(dt) #update player hunger and thirst
            self.screen.blit(self.background, (0, 0))
            self.screen.blit(pygame.transform.scale(self.background, (self.width, self.height)), (0, 0))

            if self.player.hunger == 0 or self.player.thirst == 0:
                self.state = "GAMEOVER"

            self.all_sprites.draw(self.screen) #draw sprites
            self.draw_player_stats()
            self.computer_screen.draw(self.screen)
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
        myfont = pygame.font.SysFont(None, 75)
        message = myfont.render('Game Over', False, (0, 0, 0))
        self.screen.blit(message, (250, 250))
        pygame.display.flip()
        while True:
            for event in pygame.event.get(): #make sure you can quit in gameover
                if event.type == pygame.QUIT:
                    sys.exit()

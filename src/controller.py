import sys
import pygame
import random
import math
import json
from src import player
from src import wall
from src import prop
from src.inventory import Inventory

class Controller:
    def __init__(self, width=640, height=480):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.background = pygame.Surface(self.screen.get_size()).convert()
        self.background.fill((250, 250, 250))  # set the background to white
        pygame.font.init()  # you have to call this at the start, if you want to use this module.
        pygame.key.set_repeat(1, 25)  # initialize a held keey to act as repeated key strikes
        
        self.player = player.Player()
        self.player.goto(100,100)
        
        level_data_ptr = open("src/level_data.json",'r')
        self.level_data = json.load(level_data_ptr)
        level_data_ptr.close()
        
        self.props = pygame.sprite.Group()
        self.walls = []
        self.interactables = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group((self.player,) + tuple(self.props) + tuple(self.interactables))
        self.load_level("wall_test")
        self.state = "GAME"

    
    def load_level(self, level_name):
        data = self.level_data[level_name]
        for prop_data in data["props"]:
            self.props.add(prop.Prop(prop_data[0], prop_data[1], prop_data[2], prop_data[3], prop_data[4]))
        for wall_data in data["walls"]:
            self.walls.append(wall.Wall(wall_data[0], wall_data[1], wall_data[2], wall_data[3]))
        for interactable_data in data["interactables"]:
            self.interactables.add(interactable.Interactable(interactable_data[0], interactable_data[1], interactable_data[2], interactable_data[3]))
        player_data = data["player_data"]
        self.player.goto(player_data[0], player_data[1])
        self.player.face(player_data[2])
        self.all_sprites = pygame.sprite.Group((self.player,) + tuple(self.props) + tuple(self.interactables))
        self.inventory = Inventory(self.player, 5, 5, 1)
    
    def unload_level(self):
        for prop in self.props:
            prop.kill()
        while walls:
            walls[0].pop()
        for interactable in interactables:
            interactable.kill()
    
    
    def mainLoop(self):
        while True:
            if(self.state == "GAME"):
                self.gameLoop()
            elif(self.state == "GAMEOVER"):
                self.gameOver()
    
    
    def gameLoop(self):
        loop_time = pygame.time.Clock() #keeps track of time so player knows how much to move
        loop_time.tick() #sets the time to 0
        while self.state == "GAME":
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            #if this is an event it has trouble updating when a key stops being pressed
            pressed = pygame.key.get_pressed() #allows multiple buttons to be active
            dt = loop_time.tick() #gets change in time  (dt)
            if pressed[pygame.K_w]:
                self.player.move('U', self.walls, dt)
            if pressed[pygame.K_s]:
                self.player.move('D', self.walls, dt)
            if pressed[pygame.K_a]:
                self.player.move('L', self.walls, dt)
            if pressed[pygame.K_d]:
                self.player.move('R', self.walls, dt)
            if pressed[pygame.K_i]:
                self.inventory.toggleInventory()
            # redraw the entire screen
            self.all_sprites.update()
            self.screen.blit(self.background, (0, 0))
            if self.player.hunger == 0 or self.player.thirst == 0:
                self.state = "GAMEOVER"
            self.all_sprites.draw(self.screen)
            # update the screen
            pygame.display.flip()
            self.inventory.draw(self.screen)
 
        
    def gameOver(self):
        self.player.kill()
        myfont = pygame.font.SysFont(None, 30)
        message = myfont.render('Game Over', False, (0, 0, 0))
        self.screen.blit(message, (self.width / 2, self.height / 2))
        pygame.display.flip()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

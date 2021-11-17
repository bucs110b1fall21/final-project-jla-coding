import sys
import pygame
import random
import math
from src import player

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
        
        self.all_sprites = pygame.sprite.Group((self.player,))
        
        self.state = "GAME"
    
    
    def mainLoop(self):
        while True:
            if(self.state == "GAME"):
                self.gameLoop()
            elif(self.state == "GAMEOVER"):
                self.gameOver()
    
    
    def gameLoop(self):
        while self.state == "GAME":
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    pressed = pygame.key.get_pressed() #allows multiple buttons to be active
                    if pressed[pygame.K_w]:
                        self.player.move('U', [])
                    if pressed[pygame.K_s]:
                        self.player.move('D', [])
                    if pressed[pygame.K_a]:
                        self.player.move('L', [])
                    if pressed[pygame.K_d]:
                        self.player.move('R', [])

            # redraw the entire screen
            self.all_sprites.update()
            self.screen.blit(self.background, (0, 0))
            if self.player.hunger == 0 or self.player.thirst == 0:
                self.state = "GAMEOVER"
            self.all_sprites.draw(self.screen)

            # update the screen
            pygame.display.flip()
        
        
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

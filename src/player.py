import pygame
import math
import os

class Player:
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('assets/main_character_front.png').convert_alpha()
        self.rect = self.image.get_rect() #needs to be changed because of bad collision
        
        self.rect.x = 100
        self.rect.y = 100
        
        #rect.x can't be float, so more control can be gained from a spereate x and y
        self.x = 100
        self.y = 100 
        
        self.direction = 2 #0 up, 1 left, 2 down, 3 right
        
        self.money = 0 #in cents, not dollars
        self.crypto = 0
        self.hunger = 100 #temp value, max value can be changed later
        self.thirst = 100 #see above
    
    def move(self direction): #move player
        self.direction = direction
        #note: this only moves x and y, not rect.x and rect.y
        if direction%2: self.x += self.speed * (direction - 2)
        else: self.y += self.speed * (direction - 1)
    
    def sell_crypto(self, economics, amount):
        self.money += economics.rate * amount
        self.crypto -+ amount
    
    def buy_crypto(self, economics, amount):
        self.money -= economics.rate * amount
        self.cryto += amount
    
    def update():
        #update rect pos to match x and y
        self.rect.x = int(math.round(self.x))
        self.rect.y = int(math.round(self.y))
        

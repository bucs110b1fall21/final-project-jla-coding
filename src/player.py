import pygame
import math
import os

class Player:
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('assets/main_character_front.png').convert_alpha()
        self.rect = self.image.get_rect() #needs to be changed because of bas collision
        self.rect.x = 100
        self.rect.y = 100
        self.x = 100
        self.y = 100
        self.direction = 2 #0 up, 1 left, 2 down, 3 right
        self.money = 0 #in cents, not dollars
        self.crypto = 0
        self.hunger = 100
        self.thirst = 100
    
    def move(self direction):
        self.direction = direction
        if direction%2: self.x += self.speed * (direction - 2)
        else: self.y += self.speed * (direction - 1)
    
    def sell_crypto(self, economics, amount):
        self.money += economics.rate * amount
        self.crypto -+ amount
    
    def buy_crypto(self, economics, amount):
        self.money -= economics.rate * amount
        self.cryto += amount
    
    def update():
        self.rect.x = int(math.round(self.x))
        self.rect.y = int(math.round(self.y))
        

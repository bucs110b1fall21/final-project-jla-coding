import pygame
import math

class Player(pygame.sprite.Sprite):


    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('assets/main_character_front.png').convert_alpha()
        self.rect = self.image.get_rect() #needs to be changed because of bad collision
        
        self.rect.x = 100
        self.rect.y = 100
        
        #rect.x can't be float, so more control can be gained from a spereate x and y
        self.x = 0
        self.y = 0
        
        self.direction = 2 #0 up, 1 left, 2 down, 3 right
        
        self.money = 0 #in cents, not dollars
        self.crypto = 0
        self.hunger = 100 #temp value, max value can be changed later
        self.thirst = 100 #see above
        self.inventory = []
        
        #misc stats
        self.speed = 2
        self.reach = 20 #how far away a player can reach an interactable from
    
    
    def goto(self, x, y):
        self.x = x
        self.y = y
    
    
    def move(self, direction, walls): #direction is an int 0-3 and walls is a list of walls
        #note: this only moves x and y, not rect.x and rect.y
        self.direction = direction
        for w in walls:
            if w.in_wall(self.x, self.y)
                return
        if direction%2: self.x += self.speed * (direction - 2)
        else: self.y += self.speed * (direction - 1)
        if direction == "U":
            self.rect.y -= self.speed
        elif direction == "D":
            self.rect.y += self.speed
        if direction == "L":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed
    
    
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
        

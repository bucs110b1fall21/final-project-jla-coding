import pygame

class Player(pygame.sprite.Sprite):


    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        player_img = pygame.image.load('assets/main_character_front.png').convert_alpha()
        self.image = pygame.transform.scale(player_img, (player_img.get_width()*2, player_img.get_height()*2)) #code for finding img dimentions from https://www.geeksforgeeks.org/getting-width-and-height-of-an-image-in-pygame/
        self.rect = self.image.get_rect() #needs to be changed because of bad collision
        
        self.rect.x = 100
        self.rect.y = 100
        
        #rect.x can't be float, so more control can be gained from a spereate x and y
        self.x = 0
        self.y = 0
        
        self.direction = 'D'
        
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
    
    
    def move(self, direction, walls):
        #note: this only moves x and y, not rect.x and rect.y
        self.direction = direction
        
        next_x = self.x
        next_y = self.y
        if direction == 'U': next_y -= self.speed
        elif direction == 'D': next_y += self.speed
        elif direction == 'L': next_x -= self.speed
        elif direction == 'R': next_x += self.speed
        for w in walls: #abandon movement if it moves you into a wall
            if w.in_wall(self, next_x, next_y):
                return
        self.x = next_x
        self.y = next_y
    
    

    def sell_crypto(self, economics, amount):
        self.money += economics.rate * amount
        self.crypto -+ amount
    
    
    def buy_crypto(self, economics, amount):
        self.money -= economics.rate * amount
        self.cryto += amount
    
    def update(self):
        #update rect pos to match x and y
        self.rect.x = round(self.x)
        self.rect.y = round(self.y)
        

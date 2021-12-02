import pygame

class Player(pygame.sprite.Sprite):

    
    player_sprites = {
        'U': ['assets/CharacterBack.png','assets/CharacterBack.png'],
        'D': ['assets/CharacterFront.png','assets/CharacterFront.png'],
        'L': ['assets/CharacterLeftSide.png','assets/CharacterLeftSide.png'],
        'R': ['assets/CharacterRightSide.png','assets/CharacterRightSide.png']
    }
    
    

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        player_img = pygame.image.load('assets/CharacterFront.png').convert_alpha()
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
        self.hunger = 100
        self.thirst = 100
        self.inventory = []
        #misc stats
        self.speed = 200 #measured in pixels per sec
        self.reach = 60 #how far away a player can reach an interactable from
        self.thirst_psec = -1 #thirst change per sec
        self.hunger_psec = -1 #hunger change per sec
        self.walk_animation = (0, 0)
    
    
    
    def goto(self, x, y):
        '''
            Sets the player's x and y
            args: self, int/float, int/float
            returns: None
        '''
        self.x = x
        self.y = y
    
    
    def face(self, direction):
        '''
            Sets the player's direction
            args: self, String ('U','D','L', or 'R')
            returns: None
        '''
        self.direction = direction
        self.walk_animation = (0, 0)
        next_sprite = player_sprites[direction][walk_animation[2]]
        self.image = pygame.transform.scale(next_sprite, (next_sprite.get_width()*2, next_sprite.get_height()*2)) #code for finding img dimentions from https://www.geeksforgeeks.org/getting-width-and-height-of-an-image-in-pygame/
    
    
    def move(self, direction, walls, dt): #dt = change in time in milliseconds
        '''
            Moves the player in the specified direction unless it places the player inside a wall
            args: String ('U','D','L', or 'R'), List (Walls), int/float
        '''
        #note: this only moves x and y, not rect.x and rect.y
        self.direction = direction
        next_x = self.x
        next_y = self.y
        if direction == 'U': next_y -= self.speed * dt/1000
        elif direction == 'D': next_y += self.speed * dt/1000
        elif direction == 'L': next_x -= self.speed * dt/1000
        elif direction == 'R': next_x += self.speed * dt/1000
        for w in walls: #abandon movement if it moves you into a wall
            if w.in_wall(self, next_x, next_y):
                return
        if (self.walk_animation[0] + dt)%500 < (self.walk_animation[0])%500:
            self.walk_animation = (self.walk_animation[0]+dt, direction, (walk_animation[2]+1)%2)
            next_sprite = player_sprites[direction][walk_animation[2]]
            self.image = pygame.transform.scale(next_sprite, (next_sprite.get_width()*2, next_sprite.get_height()*2)) #code for finding img dimentions from https://www.geeksforgeeks.org/getting-width-and-height-of-an-image-in-pygame/
        self.x = next_x
        self.y = next_y
    
    
    def eat(self, amount):
        '''
            Refills hunger by amount
            args: self, int/float
            returns: None
        '''
        self.hunger = self.hunger + amount
        if self.hunger > 100:
            self.hunger = 100
    
    
    def drink(self, amount):
        '''
            Refills thirst by amount
            args: self, int/float
            returns: None
        '''
        self.thirst = self.thirst + amount
        if self.thirst > 100:
            self.thirst = 100
    
    
    def update_health(self, dt):
        '''
            Updates hunger and thirst based on change in time in milliseconds
            args: self, int/float
            returns: None
        '''
        self.thirst += self.thirst_psec * dt/1000
        self.hunger += self.hunger_psec * dt/1000
    

    def sell_crypto(self, economics, amount):
        '''
            Sells amount of crypto
            args: self, Economy, int/float
            returns: None
        '''
        if self.crypto < amount: #if you overspend, sell all crypto
            amount = self.crypto
            self.crypto = 0
        else: #else just subtract the crypto
            self.crypto -= amount
        self.money += economics.rate * amount
    
    
    def buy_crypto(self, economics, amount):
        '''
            Buys amount of crypto
            args: self, Economy, int/float
            returns: None
        '''
        if money < economics.rate * amount: #if you overspend, spend all money
            amount = money / economics.rate
            self.money = 0
        else: #else just subract the money
            self.money -= economics.rate * amount
        self.cryto += amount
    
    
    def update(self):
        '''
            Update hook
            args: self
            returns: None
        '''
        #update rect pos to match x and y
        self.rect.x = round(self.x)
        self.rect.y = round(self.y)
        

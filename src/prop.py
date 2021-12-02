import pygame

class Prop(pygame.sprite.Sprite):
    
    
    def __init__(self, img_path, x, y, width, height):
        pygame.sprite.Sprite.__init__(self)
        #scale if both width and height are > 0, else don't
        if width > 0 and height > 0:
            self.image = pygame.transform.scale( pygame.image.load(img_path).convert_alpha() , (width, height) ) #creates scaled version of image input with help from https://stackoverflow.com/questions/21082145/pygame-scaling-a-sprite
        else:
            self.image = pygame.image.load(img_path).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    
    def goto(self, x, y):
        '''
            Moves sprite to specified x and y
            args: self, int, int
            returns: None
        '''
        self.rect.x = x
        self.rect.y = y

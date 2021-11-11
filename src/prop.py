import pygame

class Prop(pygame.sprite.Sprite):
    
    def __init__(self, img_path, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(img_path).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

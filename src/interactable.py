import pygame

class Interactable(pygame.sprite.Sprite):
    
    
    ID_dictionary = {"computer": 0}    
    
    
    def __init__(self, ID, img_path, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(img_path).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.ID = ID
    
    
    def attempt_interact(self, player): #this is a mess, I hope it doesn't break
        pos = player.rect.center
        #create line to test for interactions in
        if player.direction%2:
            line = (pos[0], pos[1], pos[0] + (player.direction-2*reach), pos[1])
        else:
            line = (pos[0], pos[1], pos[0], pos[1] + (player.direction-1*reach))
        #test if ranges overlap: x1 <= y2 && y1 <= x2 for range(x1,y1) and range(x2,y2)
        if (rect.left <= pos[2] and rect.right <= pos[0]) and (rect.top <= pos[3] and rect.bottom <= pos[1]):
            trigger(self)
    
    
    def trigger(self): #will cause whatever the interactable does to happen
        pass
        
        

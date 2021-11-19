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
        if player.direction == 'U':
            line = (pos[0], pos[1], pos[0], pos[1] - player.reach)
        elif player.direction == 'L':
            line = (pos[0], pos[1], pos[0] - player.reach, pos[1])
        elif player.direction == 'R':
            line = (pos[0], pos[1], pos[0], pos[1] + player.reach))
        else:
            line = (pos[0], pos[1], pos[0] + player.reach, pos[1])
        #test if ranges overlap: x1 <= y2 && y1 <= x2 for range(x1,y1) and range(x2,y2)
        #formula from https://stackoverflow.com/questions/3269434/whats-the-most-efficient-way-to-test-two-integer-ranges-for-overlap
        if (rect.left <= line[2] and rect.right <= line[0]) and (rect.top <= line[3] and rect.bottom <= line[1]):
            trigger(self)
    
    
    def trigger(self): #will cause whatever the interactable does to happen
        if self.ID == 'computer': #not sure what this will do exactly
            pass
        pass
    
        

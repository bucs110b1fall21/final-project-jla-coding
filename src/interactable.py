import pygame

class Interactable(pygame.sprite.Sprite):
    
    
    def __init__(self, ID, img_path, x, y, width, height):
        pygame.sprite.Sprite.__init__(self)
        if width > 0 and height > 0:
            self.image = pygame.transform.scale( pygame.image.load(img_path).convert_alpha() , (width, height) ) #creates scaled version of image input with help from https://stackoverflow.com/questions/21082145/pygame-scaling-a-sprite
        else:
            self.image = pygame.image.load(img_path).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.ID = ID
    
    
    def attempt_interact(self, player):
        '''
            tests to see if interaction is possible between self and player, and returns the interactable ID if it is
            args: self, Player
            returns: String or None
        '''
        pos = player.rect.center
        #create line to test for interactions in
        if player.direction == 'U':
            line = (pos[0], pos[1] - player.reach, pos[0], pos[1])
        elif player.direction == 'L':
            line = (pos[0] - player.reach, pos[1], pos[0], pos[1],)
        elif player.direction == 'R':
            line = (pos[0], pos[1], pos[0] + player.reach, pos[1])
        else:
            line = (pos[0], pos[1], pos[0], pos[1] + player.reach)
        #test if ranges overlap: x1 <= y2 && y1 <= x2 for range(x1,y1) and range(x2,y2)
        #formula from https://stackoverflow.com/questions/3269434/whats-the-most-efficient-way-to-test-two-integer-ranges-for-overlap
        if (self.rect.left <= line[2] and self.rect.right >= line[0]) and (self.rect.top <= line[3] and self.rect.bottom >= line[1]):
            return self.ID
    
        

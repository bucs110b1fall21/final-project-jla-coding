import pygame

class Button:
    def __init__(self, x, y, width, height, text, text_offset = (0,0), text_size = 22, button_color = ((50,50,50), (100,100,100)), text_color = ((255,255,255), (255,255,255))):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.text = text
        self.selected = False
        self.button_color = button_color
        self.text_color = text_color
        self.text_offset = text_offset
        self.text_size = text_size
    
    def select(self):
        self.selected = True
    
    def deselect(self):
        self.selected = False 
        
    def draw(self, screen):
        myfont = pygame.font.SysFont('Calibri', self.text_size)
        pygame.draw.rect(screen, self.button_color[int(self.selected)], (self.x, self.y, self.width, self.height))
        screen.blit( myfont.render(self.text , False, self.text_color[int(self.selected)]) ,(self.x + self.text_offset[0], self.y + self.text_offset[1]))

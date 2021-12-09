import pygame
from src import button
from src import prop

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
PERCENTAGES = (
    .05,
    .1,
    .25,
    .5,
    .75,
    .9,
    .95,
    1
)



class ComputerScreen:
    def load_screen(self):
        self.increase_button = button.Button(350, 300, 90, 30, "+", (37,-3), 50, ((75,200,75),(100,255,100)), ((200,200,200),(255,255,255)))
        self.decrease_button = button.Button(350, 400, 90, 30, "-", (40,-3), 50, ((255,75,75),(255,100,100)), ((200,200,200),(255,255,255)))
        self.buy_button = button.Button(200, 400, 75, 75, "buy", (5,10), 50, ((30,60,150),(40,75,255)), ((150,150,150),(255,255,255)))
        self.sell_button = button.Button(525, 400, 75, 75, "sell", (5,10), 50, ((150,30,30),(255,40,40)), ((150,150,150),(255,255,255)))
        self.buttons = (self.increase_button, self.decrease_button, self.buy_button, self.sell_button)

    def __init__(self, game):
        self.game = game
        self.percent_index = 3
        self.display_screen = False
        self.selection = "buy"
        self.player = game.player
        self.economy = game.economy
        self.percentage = PERCENTAGES[self.percent_index]
        self.load_screen()
    
    def toggle_display(self):
        self.display_screen = not self.display_screen
    
    def increase_percentage(self):
        if self.percent_index < 7:
            self.percent_index += 1
        self.percentage = PERCENTAGES[self.percent_index]
    
    def decrease_percentage(self):
        if self.percent_index > 0:
            self.percent_index -= 1
        self.percentage = PERCENTAGES[self.percent_index]
    
    def get_selected(self):
        output = []
        for button in buttons:
            if button.selected:
                output.append(button)
        return output
                
    
    def deselect_all(self):
        for button in self.buttons:
            button.deselect()
    
    def buy(self):
        self.player.crypto += self.player.money * self.percentage / self.economy.rate
        self.player.money = self.player.money * (1-self.percentage)
    
    def sell(self):
        self.player.money += self.player.crypto * self.percentage * self.economy.rate
        self.player.crypto = self.player.crypto * (1-self.percentage)
    
    def draw(self, screen):
        if self.display_screen:
            pygame.draw.rect(self.game.screen, (20,20,20), ((self.game.width-SCREEN_WIDTH)//2, (self.game.height-SCREEN_HEIGHT)//2, SCREEN_WIDTH, SCREEN_HEIGHT))
            for button in self.buttons:
                button.draw(self.game.screen)
            myfont = pygame.font.SysFont('Calibri', 50)
            screen.blit( myfont.render(f"{self.percentage*100}%" , False, (255,255,255)) ,(350, 350))
            self.props = (prop.Prop("assets/cashtocoin.png", 200, 300, 84, 32), prop.Prop("assets/cointocash.png", 525, 300, 84, 32), 
            prop.Prop("assets/dollar.png", 200, 150, 32, 24), prop.Prop("assets/coin.png", 200, 200, 32, 32), prop.Prop("assets/chart.png", 200, 250, 32, 32))
            myfont = pygame.font.SysFont('Calibri', 32)
            screen.blit( myfont.render(f"{int(self.player.money)/100}" , False, (255,255,255)), (250,152))
            screen.blit( myfont.render(f"{int(1000*self.player.crypto)/1000}" , False, (255,255,255)), (250,207))
            screen.blit( myfont.render(f"rate: {self.economy.rate/100}$/coin" , False, (255,255,255)), (250,250))
            for p in self.props:
                screen.blit(p.image, (p.rect.x, p.rect.y))
    

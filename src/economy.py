import math
import random

class Economy:


    def __init__(self):
        self.rate = 100 #bitcoin value
        self.history = [100] #list of previous bitcoin values
    
    
    def change_rates(self):
        '''
            Updates the rates for cash and coin
            args: self
            returns: None
        '''
        self.rate = 100 #TODO: add formula and add rate changing to game loop (!!should not run every frame!!)
        self.history.append(rate): #update history
        if len(self.history) > 20:
            self.history.pop(0)
    

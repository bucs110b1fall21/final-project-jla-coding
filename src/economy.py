import math
import random

class Economy:


    def __init__(self):
        self.rate = 100 #bitcoin value
        self.history = [100] #list of previous bitcoin values
    
    
    def change_rates(self):
        self.rate = 100 #TODO: add formula
        self.history.append(rate): #update history
        if len(self.history) > 20:
            self.history.pop(0)
    

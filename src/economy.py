import math
import random

class Economy:
    def __init__(self):
        self.rate = 100
        self.history = [100]
    
    def change_rates(self):
        self.rate = 100 #new rate goes here
        self.history.append(rate):
        if len(self.history) > 20:
            self.history.pop(0)
    

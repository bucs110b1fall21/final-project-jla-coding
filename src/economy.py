import random
import math
import pygame
#import matplotlib.pyplot as plt
#import numpy as np
 
class Economy:
 
    def __init__(self):
        self.rate = 1001 #coin value
        self.history = [1000] #list of previous coin values
        self.update_timer = 0
 
 
    def randgen(self):
        if self.rate < 1000:
            rand = int(random.randint(1, 80))
        elif self.rate > 100000:
            rand = int(random.randint(12, 100))
        else:
            rand = int(random.randint(1, 100))
        return rand
 
 #def graphing(self):
   #yaxis = []
   #yaxis.append(coin)
   #plt.pause(0.0001)
   #plt.plot(yaxis)
   #plt.show()
 
 #def ret(self):
   #returning = self.rate
   #return (returning)
    

    def changerate(self, dt):
        self.update_timer += dt
        #coin = 1000
        #i = 0
            #while i < 1:
            #print("coin= ", coin)
        if self.update_timer > 1000:
            self.update_timer -= 1000
            #if self.rate <= 0:
            #    self.rate = 0
            #    print("coin= ", self.rate)
            #    print("You are broke")
            #    exit()
            #elif coin >= 5000:
            #    self.rate = 5000
            #    print("coin= ", self.rate)
            #    print("You are rich")
            #    exit()
            #else:
            rand = self.randgen()
            if (rand == 1):
                self.rate = math.trunc(self.rate + (self.rate*1))
                #print("+100%")
                #print("coin= ", coin)
            if (1 < rand <= 3):
                self.rate = math.trunc(self.rate + (self.rate*0.69))
                #print("+69%")
                #print("coin= ", coin)
            if (3 < rand <= 6):
                self.rate = math.trunc(self.rate + (self.rate*0.42))
                #print("+42%")
                #print("coin= ", coin)
            if (6 < rand <= 12):
                self.rate = math.trunc(self.rate + (self.rate*0.25))
                #print("+25%")
                #print("coin= ", coin)
            if (12 < rand <= 25):
                self.rate = math.trunc(self.rate + (self.rate*0.15))
                #print("+10%")
                #print("coin= ", coin)
            if (25 < rand <= 40):
                self.rate = math.trunc(self.rate + (self.rate*0.05))
                #print("+5%")
                #print("coin= ", coin)
            if (40 < rand <= 55):
                self.rate = math.trunc(self.rate + (self.rate*0.02))
                #print("+2%")
                #print("coin= ", coin)
            if (55 < rand <= 60):
                self.rate = self.rate
                #print("+0%")
                #print("coin= ", coin)
            if (60 < rand <= 70):
                self.rate = math.trunc(self.rate - (self.rate*0.02))
                #print("-2%")
                #print("coin= ", coin)
            if (70 < rand <= 80):
                self.rate = math.trunc(self.rate - (self.rate*0.05))
                #print("-5%")
                #print("coin= ", coin)
            if (80 < rand <= 95):
                self.rate = math.trunc(self.rate - (self.rate*0.1))
                #print("-10%")
                #print("coin= ", coin)
            if (95 < rand <= 99):
                self.rate = math.trunc(self.rate - (self.rate*0.25))
                #print("-25%")
                #print("coin= ", coin)
            if (rand == 100):
                self.rate = math.trunc(self.rate - (self.rate*0.5))
                #print("-50%")
                #print("coin= ", coin)
                #print("coin= ", self.rate)
            self.history.append(self.rate)

        return self.rate
    
       

 
 



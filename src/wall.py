class Wall: #Note: 
    def __init__(self, x1, y1, x2, y2): #(x1,y1) is top left, (x2,y2) is bottom right
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
    
    def in_wall(self, x, y):
        return x > x1 and x < x2 and y > y1 and y < y2

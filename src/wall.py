class Wall: #Note: not a sprite and invisable. If you want a sprite with collision, make a prop and but a wall over it


    def __init__(self, x1, y1, x2, y2): #(x1,y1) is top left, (x2,y2) is bottom right
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
    
    
    def in_wall(self, x, y):
        #formula from https://stackoverflow.com/questions/3269434/whats-the-most-efficient-way-to-test-two-integer-ranges-for-overlap
        return x > x1 and x < x2 and y > y1 and y < y2

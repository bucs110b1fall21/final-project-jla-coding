class Wall: #Note: not a sprite and invisable. If you want a sprite with collision, make a prop and but a wall over it


    def __init__(self, x1, y1, x2, y2): #(x1,y1) is top left, (x2,y2) is bottom right
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
    
    
    def in_wall(self, player, next_x, next_y):
        #formula x1 <= y2 && y1 <= x2 for range(x1,y1) and range(x2,y2) is from https://stackoverflow.com/questions/3269434/whats-the-most-efficient-way-to-test-two-integer-ranges-for-overlap
        return next_x <= self.x2 and next_x + player.rect.width >= self.x1 and next_y <= self.y2 and next_y + player.rect.height >= self.y1

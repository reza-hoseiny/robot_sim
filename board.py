class Board():
    def __init__(self,lb=0, rb=4, tb=0, bb=4):
        self.left_boundary = lb
        self.right_boundary = rb
        self.top_boundary = tb
        self.bottom_boundary = bb
    
    def within_boundaries(self, position):
        x_coord, y_coord = position.coordinates()
        if x_coord > self.left_boundary and x_coord < self.right_boundary:
            if y_coord > self.bottom_boundary and y_coord < self.top_boundary:
                return True 
        return False






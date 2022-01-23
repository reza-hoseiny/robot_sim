class Board:
    def __init__(self, lb=0, rb=4, tb=0, bb=4):
        self.left_boundary = lb
        self.right_boundary = rb
        self.top_boundary = tb
        self.bottom_boundary = bb
        self.occupied_positions = []

    def within_boundaries(self, position):
        x_coord, y_coord = position.coordinates()
        if x_coord > self.left_boundary and x_coord < self.right_boundary:
            if y_coord > self.bottom_boundary and y_coord < self.top_boundary:
                return True
        return False

    def occupy(self, position):
        self.occupied_positions.append(position)

    def space_empty(self, position):
        if self.occupied_positions.include(position):
            return False
        return True

from face import Face

class Robot:
    def __init__(self, name="simple robot"):
        self.name= name
        self.current_x = None
        self.current_y = None
        self.table= None
        self.face_direction= None

    def getName(self):
        return self.name

    def setPosition(self, x, y):
        x_table_dim, y_table_dim = self.getTableDimensions() #instead of self.table.getDimensions()
        if x_table_dim is not None:
            if x>=0 and x <= x_table_dim:
                self.current_x = x
        if y_table_dim is not None:
            if y>=0 and y <= y_table_dim:
                self.current_y = y

    def getCurrentPosition(self):
        return (self.current_x, self.current_y)

    def setFaceDirection(self, face_direction):
        if face_direction in Face.__members__.values():
            self.face_direction = face_direction
        else:
            raise ValueError("the given face direction must be a valid value of Face enum")

    def getCurrentFaceDirection(self):
        return self.face_direction

    def setTable(self, table):
        self.table = table

    def getTable(self):
        return self.table

    def getTableDimensions(self):
        if self.table is not None:
            dim = self.table.getDimensions()
            return dim
        else:
            return None

    def is_not_on_table(self):
        x_current, y_current = self.getCurrentPosition()
        face_current = self.getCurrentFaceDirection()
        if (x_current is None) or (y_current is None) or (face_current is None):
            return True
        else:
            return False

    def move(self):
        x_current, y_current = self.getCurrentPosition()
        face_current = self.getCurrentFaceDirection()
        (x_table_dim, y_table_dim) =  self.getTableDimensions()
        
        if self.is_not_on_table():
            return #A robot that is not on the table can choose to ignore the MOVE, LEFT, RIGHT and REPORT commands
        if face_current==Face.NORTH:
            if y_current < y_table_dim-1:
                self.current_y += 1
            #otherwise ignore the move command
        elif face_current==Face.SOUTH:
            if y_current > 0 :
                self.current_y -= 1
            #otherwise ignore the move command
        elif face_current==Face.EAST:
            if x_current < x_table_dim-1:
                self.current_x += 1
            #otherwise ignore the move command
        elif face_current==Face.WEST:
            if x_current > 0:
                self.current_x -= 1
            #otherwise ignore the move command
        else:
            raise ValueError("the given face direction is not a valid value from Face enum")
        
    def report(self):
        x_current, y_current = self.getCurrentPosition()
        face_current = self.getCurrentFaceDirection()
        return (x_current, y_current,face_current)

    def left(self):
        """
        LEFT command forces the robot to rotate 90 degrees in the left direction without changing the position of the robot
        """
        if self.is_not_on_table():
            return #A robot that is not on the table can choose to ignore the MOVE, LEFT, RIGHT and REPORT commands
        face_current = self.getCurrentFaceDirection()
        if face_current == Face.NORTH:
            self.face_direction = Face.WEST
        elif face_current == Face.SOUTH:
            self.face_direction = Face.EAST
        elif face_current == Face.EAST:
            self.face_direction = Face.NORTH
        elif face_current == Face.WEST:
            self.face_direction = Face.SOUTH

    def right(self):
        """
        RIGHT command forces the robot to rotate 90 degrees in the right direction without changing the position of the robot
        """
        if self.is_not_on_table():
            return #A robot that is not on the table can choose to ignore the MOVE, LEFT, RIGHT and REPORT commands

        face_current = self.getCurrentFaceDirection()
        if face_current == Face.NORTH:
            self.face_direction = Face.EAST
        elif face_current == Face.SOUTH:
            self.face_direction = Face.WEST
        elif face_current == Face.EAST:
            self.face_direction = Face.SOUTH
        elif face_current == Face.WEST:
            self.face_direction = Face.NORTH



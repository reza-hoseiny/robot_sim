from face import Face

class Robot:
    def __init__(self, name="simple robot"):
        self.name= name
        self.current_x = None
        self.current_y = None
        self.table= None
        self.face_direction= None
        pass

    def getName(self):
        return self.name

    def setPosition(self, x, y):
        self.current_x = x
        self.current_y = y

    def getCurrentPosition(self):
        return (self.current_x, self.current_y)
        pass


    def setFaceDirection(self, face_direction):
        if face_direction in Face.__members__.values():
            self.face_direction = face_direction
        else:
            raise ValueError("the given face direction must be a valid value of Face enum")
        pass

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

    def move(self):
        x_current, y_current = self.getCurrentPosition()
        face_current = self.getCurrentFaceDirection()
        (x_table_dim, y_table_dim) =  self.getTableDimensions()
        if face_current==Face.NORTH:
            if y_current < y_table_dim:
                self.current_y += 1
            #otherwise ignore the move command
        elif face_current==Face.SOUTH:
            if y_current > 0 :
                self.current_y -= 1
            #otherwise ignore the move command
        elif face_current==Face.EAST:
            if x_current < x_table_dim:
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





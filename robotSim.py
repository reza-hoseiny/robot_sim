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

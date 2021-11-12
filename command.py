from commandType import CommandType

class Command():
    def __init__(self):
        self.commandType = None

    def getCommandType(self):
        return self.commandType

class PlaceCommand(Command):
    def __init__(self, x, y, face_direction):
        self.commandType = CommandType.PLACE
        self.x_position = x
        self.y_position = y
        self.face_direction = face_direction


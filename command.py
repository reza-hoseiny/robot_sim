from typing import Tuple
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

    def set_x_y_valid_boundaries(self, x_min, y_min, x_max, y_max):
        self.x_min = x_min
        self.y_min = y_min
        self.x_max = x_max
        self.y_max = y_max
    
    def is_valid(self):
        if (self.x_position > self.x_max) or (self.x_position<self.x_min):
            return False
        if (self.y_position > self.y_max) or (self.y_position<self.y_min):
            return False
        return True

class MoveCommand(Command):
    def __init__(self):
        self.commandType = CommandType.MOVE
        
class LeftCommand(Command):
    def __init__(self):
        self.commandType = CommandType.LEFT        

class RightCommand(Command):
    def __init__(self):
        self.commandType = CommandType.RIGHT

class RerportCommand(Command):
    def __init__(self):
        self.commandType = CommandType.REPORT
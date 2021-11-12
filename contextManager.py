from commandType import CommandType
from robot import Robot
from face import Face
from table import Table
from command import *

class ContextManager():
    def __init__(self, table, robot):
        self.table = table
        self.robot = robot
        self.robot.setTable(self.table)

    def getTable(self):
        return self.table
    
    def getRobot(self):
        return self.robot

    def issue(self,command):
        result = None
        ctype = command.getCommandType() 
        if ctype == CommandType.PLACE:
            (x_max, y_max) = self.table.getDimensions()
            command.set_x_y_valid_boundaries(0,0,x_max,y_max)
            if command.is_valid():
                self.robot.setPosition(command.x_position, command.y_position)
                self.robot.setFaceDirection(command.face_direction)
        elif ctype == CommandType.MOVE:
            self.robot.move()
        elif ctype == CommandType.LEFT:
            self.robot.left()
        elif ctype == CommandType.RIGHT:
            self.robot.right()
        elif ctype == CommandType.REPORT:
            result = self.robot.report()
        return result

                
                



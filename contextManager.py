import sys
from unittest import result
from commandType import CommandType
from robot import Robot
from face import Face
from table import Table
from command import *

class ContextManager():
    def __init__(self, table, robot, input_file_name=sys.stdin):
        self.table = table
        self.robot = robot
        self.robot.setTable(self.table)
        self.input_file_name = input_file_name
        
            
    def parse(self, line):
        valid_str_commands = ["PLACE", "MOVE", "LEFT", "RIGHT", "REPORT"]
        valid_command = False
        command = None
        for valid_str_command in valid_str_commands:
            if line.startswith(valid_str_command):
                valid_command= True
            if line.startswith("MOVE"):
                command = MoveCommand()
            if line.startswith("LEFT"):
                command = LeftCommand()
            if line.startswith("RIGHT"):
                command = RightCommand()
            if line.startswith("REPORT"):
                command = ReportCommand()
            if line.startswith("PLACE"):
                # we need to find out what is x,y,f?
                second_part = line.split(" ")[1]
                params = second_part.split(",")
                x_init = int(params[0])
                y_init = int(params[1])
                face_direction_str = params[2]                
                if face_direction_str.upper() == "NORTH":
                    face_direction = Face.NORTH
                elif face_direction_str.upper() == "SOUTH":
                    face_direction = Face.SOUTH
                elif face_direction_str.upper() == "WEST":
                    face_direction = Face.WEST
                elif face_direction_str.upper() == "EAST":
                    face_direction = Face.EAST
                command = PlaceCommand(x_init,y_init,face_direction)
        if not valid_command:
            return None
        return command

    def execute_commands(self):
        try:
            self.input_file_hanlder = open(self.input_file_name, mode="r")
            try:
                lines = self.input_file_hanlder.read().splitlines() # List with stripped line-breaks
                result = None
                for line in lines:
                    command = self.parse(line)
                    if command is not None:
                        result = self.issue(command)
            except IOError:
                print("Unable to read commans from input file.")
            finally:
                self.input_file_hanlder.close()
        except IOError:
            print("Unable to open and read the input file")
        return result
                        
        
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

                
                




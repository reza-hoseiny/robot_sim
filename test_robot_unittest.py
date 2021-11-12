#!/usr/bin/env python
import unittest                 #Import unittest from the standard library of python
from robot import Robot
from face import Face
from table import Table

class TestRobotMethods(unittest.TestCase):  #every test class must inherit from the TestCase class
    """
    This is the basic test class for the Robot class
    Any method which starts with ``test_`` will considered as a test case in the unittest frameowrk...
    """
    def setUp(self):
        self.robot_name = 'The first robot'
        self.robot = Robot(self.robot_name)
        self.x_initial, self.y_initial = 0,0
        self.robot.setPosition(self.x_initial, self.y_initial)
        self.face_initial = Face.EAST
        self.robot.setFaceDirection(self.face_initial)
        # fabricate a table of dimensions 5 units x 5 units and pass it to the robot
        self.x_dimension_table = 5
        self.y_dimension_table = 5
        self.test_table_one = Table("table one", self.x_dimension_table, self.y_dimension_table)
        self.robot.setTable(self.test_table_one)
        

    def test_name(self):
        self.assertEqual(self.robot.getName(), self.robot_name)
    
    def test_position(self):
        self.assertEqual(self.robot.getCurrentPosition(), (self.x_initial, self.y_initial))

    def test_face(self):
        self.assertEqual(self.robot.getCurrentFaceDirection(), self.face_initial)

    def test_set_table(self):
        self.assertEqual(self.robot.getTable().getTableName(), "table one")

    def test_get_table_dimensions(self):
        (x_dim,y_dim) = self.robot.getTableDimensions()
        self.assertEqual((x_dim,y_dim), (self.x_dimension_table, self.y_dimension_table))

    def test_move(self): 
        """
        test the move function of the toy robot to see if it moves just one unit forward in the direction it is currently facing.
        """
        (x_table_dim, y_table_dim) =  self.robot.getTableDimensions()
        x_current, y_current = self.robot.getCurrentPosition()
        face_current = self.robot.getCurrentFaceDirection()
        self.robot.move()
        x_after_move , y_after_move = self.robot.getCurrentPosition()
        if face_current==Face.NORTH:
            if y_current == y_table_dim:
                self.assertEqual((x_after_move , y_after_move), (x_current, y_current))     #skip move
            else:
                self.assertEqual((x_after_move , y_after_move), (x_current, y_current+1))
        elif face_current==Face.SOUTH:
            if y_current == 0:
                self.assertEqual((x_after_move , y_after_move), (x_current, y_current))     #skip move
            else:
                self.assertEqual((x_after_move , y_after_move), (x_current, y_current-1))
        elif face_current==Face.EAST:
            if x_current == x_table_dim:
                self.assertEqual((x_after_move , y_after_move), (x_current, y_current))     #skip move
            else:
                self.assertEqual((x_after_move , y_after_move), (x_current+1, y_current))
        elif face_current==Face.WEST:
            if x_current == 0:
                self.assertEqual((x_after_move , y_after_move), (x_current, y_current))     #skip move
            else:
                self.assertEqual((x_after_move , y_after_move), (x_current-1, y_current))
        else:
            self.assertRaises(ValueError, None) # the code must raise ValueError("the given face direction is not a valid value from Face enum")
        
    def test_report(self): 
        """
        REPORT function should announce the X,Y coordicnate and the orientation of the robot.
        """
        x_current, y_current = self.robot.getCurrentPosition()
        face_current = self.robot.getCurrentFaceDirection()
        x_report, y_report, face_report = self.robot.report()
        self.assertEqual((self.x_initial, self.y_initial, self.face_initial), (x_report, y_report, face_report))
        self.assertEqual((x_current, y_current, face_current), (x_report, y_report, face_report))
        
        self.robot.move()   #assuming that the inital face is Face.EAST
        x_report, y_report, face_report = self.robot.report() #after move
        self.assertEqual((self.x_initial+1, self.y_initial, self.face_initial), (x_report, y_report, face_report))

    def test_left(self):
        """
        LEFT command should rotate the robot 90 degrees in the specified direction without changing the position of the robot
        """
        x_current, y_current = self.robot.getCurrentPosition()
        face_current = self.robot.getCurrentFaceDirection()
        self.robot.left()
        x_current_after_command, y_current_after_command = self.robot.getCurrentPosition()
        face_current_after_command = self.robot.getCurrentFaceDirection()
        face_correct_after_left = None
        if face_current == Face.NORTH:
            face_correct_after_left = Face.WEST
        elif face_current == Face.SOUTH:
            face_correct_after_left = Face.EAST
        elif face_current == Face.EAST:
            face_correct_after_left = Face.NORTH
        elif face_current == Face.WEST:
            face_correct_after_left = Face.SOUTH
        self.assertEqual((x_current_after_command, y_current_after_command, face_current_after_command), (x_current, y_current, face_correct_after_left))
        

    def test_right(self):
        """
        RIGHT command should rotate the robot 90 degrees in the RIGHT direction without changing the position of the robot
        """
        x_current, y_current = self.robot.getCurrentPosition()
        face_current = self.robot.getCurrentFaceDirection()
        self.robot.right()
        x_current_after_command, y_current_after_command = self.robot.getCurrentPosition()
        face_current_after_command = self.robot.getCurrentFaceDirection()
        if face_current == Face.NORTH:
            face_correct_after_right = Face.EAST
        elif face_current == Face.SOUTH:
            face_correct_after_right = Face.WEST
        elif face_current == Face.EAST:
            face_correct_after_right = Face.SOUTH
        elif face_current == Face.WEST:
            face_correct_after_right = Face.NORTH
        self.assertEqual((x_current_after_command, y_current_after_command, face_current_after_command), (x_current, y_current, face_correct_after_right))
        
    def test_case_one(self):
        """
        a simple test case for the following command series:
        PLACE 0,0,NORTH
        MOVE
        REPORT
        the expected Output is 0,1,NORTH
        """
        self.robot.setPosition(0,0)
        self.robot.setFaceDirection(Face.NORTH)
        self.robot.move()
        x_report, y_report, face_report = self.robot.report()
        self.assertEqual((0, 1, Face.NORTH), (x_report, y_report, face_report))

    def test_case_two(self):
        """
        a simple test case for the following command series:
        PLACE 0,0,NORTH
        LEFT
        REPORT
        the expected Output is 0,0,WEST
        """
        self.robot.setPosition(0,0)
        self.robot.setFaceDirection(Face.NORTH)
        self.robot.left()
        x_report, y_report, face_report = self.robot.report()
        self.assertEqual((0, 0, Face.WEST), (x_report, y_report, face_report))

    def test_case_three(self):
        """
        a simple test case for the following command series:
        PLACE 1,2,EAST
        MOVE
        MOVE
        LEFT
        MOVE
        REPORT
        the expected Output is 3,3,NORTH
        """
        self.robot.setPosition(1,2)
        self.robot.setFaceDirection(Face.EAST)
        self.robot.move()
        self.robot.move()
        self.robot.left()
        self.robot.move()
        x_report, y_report, face_report = self.robot.report()
        self.assertEqual((3, 3, Face.NORTH), (x_report, y_report, face_report))


    def test_edge_case_table(self):
        """
        edge case input for table x&y dimension:
        x_dimension and y_dimension of table cannot be negative or equal to zero
        if an invalid input is given, application should raise an error and stops the program
        check that Table and setTable fails when the table x_dimension and y_dimension are negative or equal to zero
        """
        with self.assertRaises(ValueError):
            test_table_invalid = Table("name of a invalid table", 0, 0)
            self.robot.setTable(test_table_invalid)
        
        with self.assertRaises(ValueError):
            test_table_invalid = Table("name of a invalid table", -1, 5)
        
        with self.assertRaises(ValueError):
            test_table_invalid = Table("name of a invalid table", 1, -5)
        
        with self.assertRaises(ValueError):
            test_table_invalid = Table("name of a invalid table", 1, 0)

        with self.assertRaises(ValueError):
            test_table_invalid = Table("name of a invalid table", 0, 1)

    def test_edge_case_initial_robot_position(self):
        """
        edge case input for robot x&y initial positions:
        setPosition[x_ and y] of robot cannot be negative, it must not be larger than the table x_dimension and y_dimension too
        if an invalid input is given, application should not set the position of x_ and y, i.e. set them to None, and then hope that in future a valid input is given        
        """

        self.robot.setPosition(0, 0)
        x_current , y_current = self.robot.getCurrentPosition()
        self.assertEqual((0,0),(x_current , y_current))
        
        self.robot = Robot('Second robot')
        self.robot.setPosition(-5, -5)        
        x_current , y_current = self.robot.getCurrentPosition()
        self.assertEqual((None,None),(x_current , y_current))

        self.robot = Robot('Third robot')
        self.robot.setPosition(0, -5)        
        x_current , y_current = self.robot.getCurrentPosition()
        self.assertEqual((0,None),(x_current , y_current))

        self.robot = Robot('Furth robot')
        self.robot.setPosition(-4, 0)        
        x_current , y_current = self.robot.getCurrentPosition()
        self.assertEqual((None,0),(x_current , y_current))

        self.robot = Robot('Fifth robot')   #check if position of robot is more than the table size
        self.robot.setPosition(6, 6)        
        x_current , y_current = self.robot.getCurrentPosition()
        self.assertEqual((None,None),(x_current , y_current))



if __name__ == '__main__':
    unittest.main()

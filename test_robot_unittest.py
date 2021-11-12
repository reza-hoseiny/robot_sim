#!/usr/bin/env python
import unittest                 #Import unittest from the standard library of python
from robotSim import Robot
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



        








if __name__ == '__main__':
    unittest.main()

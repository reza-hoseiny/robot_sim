#!/usr/bin/env python
import unittest                 #Import unittest from the standard library of python
from robotSim import Robot
from face import Face

class TestRobotMethods(unittest.TestCase):  #every test class must inherit from the TestCase class
    """
    This is the basic test class for the Robot class
    Any method which starts with ``test_`` will considered as a test case in the unittest frameowrk...
    """
    def setUp(self):
        self.robot_name = 'The first robot'
        self.robot = Robot(self.robot_name)
        self.x_initial, self.y_initial = 0,0
        self.face_initial = Face.EAST


    def test_name(self):
        self.assertEqual(self.robot.getName(), self.robot_name)
    
    def test_position(self):
        self.robot.setPosition(self.x_initial, self.y_initial)
        self.assertEqual(self.robot.getCurrentPosition(), (self.x_initial, self.y_initial))

    def test_face(self):
        self.robot.setFaceDirection(self.face_initial)
        self.assertEqual(self.robot.getCurrentFaceDirection(), self.face_initial)




if __name__ == '__main__':
    unittest.main()

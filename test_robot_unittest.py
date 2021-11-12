#!/usr/bin/env python
import unittest                 #Import unittest from the standard library of python
from robotSim import Robot

class TestRobotMethods(unittest.TestCase):  #every test class must inherit from the TestCase class
    """
    This is the basic test class for the Robot class
    Any method which starts with ``test_`` will considered as a test case in the unittest frameowrk...
    """
    def setUp(self):
        self.robot_name = 'The first robot'
        self.robot = Robot(self.robot_name)


    def test_report(self):
        self.assertEqual(self.robot.getName(), self.robot_name)

if __name__ == '__main__':
    unittest.main()

# robot_sim

We follow Test-driven development `(TDD)` that is a software development process relying on software requirements being converted to test cases before software is fully developed, and tracking all software development by repeatedly testing the software against all test cases.

the main entry for the test cases can be found in `test_robot_unittest.py` file. 
To run this file, run `python test_robot_unittest.py` from the command line. (or use `python test_robot_unittest.py -v`) to see which test cases are currently running with more details on the screen.


The main enrty to run the main.py file is to run `python main.py` and then it asks the user to enter the name of a file which contians all the commands. (say commands.txt as example)
Then main.py creates a `ContextManager` class and then asks it to execute all commands in the input file line by line and then print out the result of execution. 

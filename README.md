# robot_sim

# Toy Robot Simulator
 
## Description

A simulation of a toy robot moving on a square tabletop, of dimensions 5 units x 5 units.  See [Specification](#specification) below for details.

All code is written in Ruby, with some help from [ActiveModel::Validations](http://api.rubyonrails.org/classes/ActiveModel/Validations.html) for model validation checks, and [Thor](https://github.com/wycats/thor) for the command-line interface. 

## Usage

Input commands manually on command line:

    $ toy_robot


Run commands from a file:

    $ toy_robot -f [filename]

### Description
- The application is a simulation of a toy robot moving on a square tabletop, of dimensions 5 units x 5 units.
- There are no other obstructions on the table surface.
- The robot is free to roam around the surface of the table, but must be prevented from falling to destruction. Any movement
that would result in the robot falling from the table must be prevented, however further valid movement commands must still
be allowed.

*Create an application that can read in commands of the following form*  
`PLACE X,Y,F`  
`MOVE`  
`LEFT`  
`RIGHT`  
`REPORT`  

- `PLACE` will put the toy robot on the table in position `X,Y` and facing `NORTH`, `SOUTH`, `EAST` or `WEST`.
- The origin (`0,0`) can be considered to be the `SOUTH WEST` most corner.
- The first valid command to the robot is a `PLACE` command, after that, any sequence of commands may be issued, in any order, including another `PLACE` command. The application should discard all commands in the sequence until a valid `PLACE` command has been executed
- `MOVE` will move the toy robot one unit forward in the direction it is currently facing.
- `LEFT` and `RIGHT` will rotate the robot 90 degrees in the specified direction without changing the position of the robot.
- `REPORT` will announce the `X`,`Y` and `F` of the robot. This can be in any form, but standard output is sufficient.

<ul>
<li>A robot that is not on the table can choose to ignore the <code>MOVE</code>, <code>LEFT</code>, <code>RIGHT</code> and <code>REPORT</code> commands.</li>
<li>Input can be from a file, or from standard input, as the developer chooses.</li>
<li>Provide test data to exercise the application.</li>
</ul>

### Constraints
The toy robot must not fall off the table during movement. This also includes the initial placement of the toy robot.
Any move that would cause the robot to fall must be ignored.

Example Input and Output:  
a)  
`PLACE 0,0,NORTH`  
`MOVE`  
`REPORT`  
Output: `0,1,NORTH`  

b)  
`PLACE 0,0,NORTH`  
`LEFT`  
`REPORT`  
Output: `0,0,WEST`  

c)  
`PLACE 1,2,EAST`  
`MOVE`  
`MOVE`  
`LEFT`  
`MOVE`  
`REPORT`  
Output: `3,3,NORTH`

### Visual Map of Board

The `MAP [ROBOT_NAME] [BOARD]` command shows a visual map of the board from three perspectives:

- `MAP` by itself shows the full map of the board, including the position and direction of all robots on the board (`Λ > V <`) and all the blocks they have placed (`█`).  For example:

           0   1   2   3   4
        4 [ ] [ ] [ ] [█] [ ]
        3 [ ] [ ] [█] [V] [█]
        2 [ ] [█] [ ] [█] [ ]
        1 [█] [Λ] [█] [ ] [ ]
        0 [ ] [█] [ ] [ ] [ ]
        Robots on the Board:
        Name: Kryten
        Kryten's Position: 1,1,NORTH
        Kryten's Blocks at Positions:
        [0, 1], [1, 0], [1, 2],
        [2, 1]
        -------
        Name: Marvin
        Marvin's Position: 3,3,SOUTH
        Marvin's Blocks at Positions:
        [2, 3], [3, 2], [3, 4],
        [4, 3]
        -------

- `MAP ROBOT_NAME` shows the map from the robot's perspective.  The robot knows only about the position and direction of itself, as well as the locations of all blocks it has placed, but still cannot move to spaces occupied by another robot or its blocks.  For the example above:

        > MAP Kryten

           0   1   2   3   4
        4 [ ] [ ] [ ] [ ] [ ]
        3 [ ] [ ] [ ] [ ] [ ]
        2 [ ] [█] [ ] [ ] [ ]
        1 [█] [Λ] [█] [ ] [ ]
        0 [ ] [█] [ ] [ ] [ ]
        Kryten's Position: 1,1,NORTH
        Kryten's Blocks at Positions:
        [0, 1], [1, 0], [1, 2],
        [2, 1]

        > MAP Marvin

           0   1   2   3   4
        4 [ ] [ ] [ ] [█] [ ]
        3 [ ] [ ] [█] [V] [█]
        2 [ ] [ ] [ ] [█] [ ]
        1 [ ] [ ] [ ] [ ] [ ]
        0 [ ] [ ] [ ] [ ] [ ]
        Marvin's Position: 3,3,SOUTH
        Marvin's Blocks at Positions:
        [2, 3], [3, 2], [3, 4],
        [4, 3]

- `MAP BOARD` shows the map from the board's perspective.  The board knows about the spaces on the board that are occupied by an object (×), without any specifics of the object.  For the example above:

           0   1   2   3   4
        4 [ ] [ ] [ ] [×] [ ]
        3 [ ] [ ] [×] [×] [×]
        2 [ ] [×] [ ] [×] [ ]
        1 [×] [×] [×] [ ] [ ]
        0 [ ] [×] [ ] [ ] [ ]
        Occupied Positions:
        [0, 1], [1, 0], [1, 1],
        [1, 2], [2, 1], [2, 3],
        [3, 2], [3, 3], [3, 4],
        [4, 3]

- - -


## Installation


We follow Test-driven development `(TDD)` that is a software development process relying on software requirements being converted to test cases before software is fully developed, and tracking all software development by repeatedly testing the software against all test cases.

the main entry for the test cases can be found in `test_robot_unittest.py` file. 
To run this file, run `python test_robot_unittest.py` from the command line. (or use `python test_robot_unittest.py -v`) to see which test cases are currently running with more details on the screen.


The main enrty to run the main.py file is to run `python main.py` and then it asks the user to enter the name of a file which contians all the commands. (say commands.txt as example)
Then main.py creates a `ContextManager` class and then asks it to execute all commands in the input file line by line and then print out the result of execution. 

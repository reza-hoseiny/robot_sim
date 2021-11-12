from enum import Enum, unique

@unique
class CommandType(Enum):   
    PLACE= 1
    MOVE=2
    LEFT=3
    RIGHT=4
    REPORT=5


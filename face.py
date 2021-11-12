from enum import Enum, unique

@unique
class Face(Enum):   
    #unique decorator specifically for enumerations to prevent duplicate values in Enum 
    NORTH= 1
    SOUTH= 2
    EAST= 3
    WEST= 4  

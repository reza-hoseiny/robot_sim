from contextManager import ContextManager
from robot import Robot
from face import Face
from table import Table

def main():
    print("\n================================\nA simulation of a toy robot moving on a square tabletopd!\n================================\n")
    # print("Enter the input file name to read the input commands")
    file_name = input('Enter input file name that contains the commands:')
    contextManager = ContextManager(Table("Table", 5, 5), Robot("Robot"),file_name)
    result = contextManager.execute_commands()
    print("\nOutput: ", result)

if __name__ == "__main__":
    main()

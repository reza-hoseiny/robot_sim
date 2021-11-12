class ContextManager():
    def __init__(self, table, robot):
        self.table = table
        self.robot = robot
        self.robot.setTable(self.table)

    def getTable(self):
        return self.table
    
    def getRobot(self):
        return self.robot


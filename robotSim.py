class Robot:
    def __init__(self, name="simple robot"):
        self.name= name
        self.current_x = None
        self.current_y = None
        pass

    

    def getName(self):
        return self.name

    def setPosition(self, x, y):
        self.current_x = x
        self.current_y = y


    def getCurrentPosition(self):
        return (self.current_x, self.current_y)
        pass

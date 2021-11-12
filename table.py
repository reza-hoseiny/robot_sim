class Table():
    def __init__(self, name="simple table", x_dimension=10, y_dimension=10):
        self.name   = name
        self.x_dimension = x_dimension
        self.y_dimension = y_dimension

    def getTableName(self):
        return self.name   

    def getDimensions(self):
        return (self.x_dimension, self.y_dimension)
class Table():
    def __init__(self, name="simple table", x_dimension=10, y_dimension=10):
        self.name = name
        if (x_dimension>0) and (y_dimension>0):
            self.x_dimension = x_dimension
            self.y_dimension = y_dimension
        else:
            raise ValueError("the given x or y dimension of table is not positive")

    def getTableName(self):
        return self.name   

    def getDimensions(self):
        return (self.x_dimension, self.y_dimension)
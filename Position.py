class Position:
    def __init__(self, row, column):
        self.row = row
        self.column = column

    def updatePosition(self, rowSteps, colSteps):
        self.row+=rowSteps
        self.column+=colSteps
    
    def updateRow(self, steps):
        self.row+=steps

    def updateCol(self, steps):
        self.column+=steps
    
    def getRow(self):
        return self.row
    
    def getCol(self):
        return self.column
    
    def __str__(self):
        return "Row: "+str(self.row)+" Column: "+str(self.column)
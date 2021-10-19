class matrix:
    def __init__(self, xdim, ydim, numbers):
        self.row = xdim
        self.column = ydim
        self.values = __create__(self.row, self.column, numbers)
    
    def __str__(self):
        outtie = ""
        for k in range(self.column):
           outtie += str(self.values[k]) + "\n"
        return(outtie)
    
    def dex(self, y = 0, x = 0):
        if bool(x) and bool(y):
            return(self.values[y-1][x-1])
        elif bool(y):
            return(self.values[y-1])
        elif bool(x):
            outtie = []
            for k in range(self.column):
                outtie.append(self.values[k][x-1])
            return(outtie)

    
def __create__(row, column, numbers):
    listed = []
    for k in range(column):
        listed.append([])
        for i in range(row):
            listed[k].append(numbers[i])
        del numbers[0:row]
    return(listed)

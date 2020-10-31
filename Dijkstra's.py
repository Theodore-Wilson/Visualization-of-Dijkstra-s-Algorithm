class testDijkstra():
    def __init__(self, r, c):
        self.row = r
        self.col = c
        self.startRow = 0
        self.startCol = 0
        self.endRow = r-1
        self.endCol = c-1
        self.grid = []
        self.visited = []
        self.finalPath = []

    def getStartRow(self):
        return self.startRow
    
    def getStartCol(self):
        return self.startCol
    
    def getEndRow(self):
        return self.endRow
    
    def getEndCol(self):
        return self.endCol

    def getGrid(self):
        return self.grid

    def getVisited(self):
        return self.visited
    
    def getFinalPath(self):
        return self.finalPath

    def checkRight(self, currentCol, maxColNumber):
        if currentCol + 1 <= maxColNumber:
            return True
        return False

    def checkLeft(self, currentCol, minColNumber):
        if currentCol - 1 >= minColNumber:
            return True
        return False

    def checkTop(self, currentRow, minRowNumber):
        if currentRow - 1 >= minRowNumber:
            return True
        return False

    def checkBottom(self, currentRow, maxRowNumber):
        if currentRow + 1 <= maxRowNumber:
            return True
        return False

    def checkEnd(self, currentRow, currentCol, finishRow, finishCol):
        if currentRow == finishRow and currentCol == finishCol:
            return True
        return False

    def createGrid(self):
        self.startLoc = Node(self.startRow, self.startCol)
        self.endLoc = Node(self.endRow, self.endCol)
        self.grid = [[Node(j, i) for i in range(self.col)] for j in range(self.row)]
        self.grid[self.startRow][self.startCol].setVisited(True)
        self.grid[self.startRow][self.startCol].setDis(0)
        
    def setWalls(self, row, col):
        return

    def shortestPath(self):
        self.finalPath = [self.grid[self.startRow][self.startCol]]
        while (self.finalPath[0].getRow() != self.endRow or self.finalPath[0].getCol() != self.endCol):
            if self.finalPath[0].getUpPath() == None:
                if self.checkTop(self.finalPath[0].getRow(), 0):
                    if self.grid[self.finalPath[0].getRow()-1][self.finalPath[0].getCol()].getDis() > self.finalPath[0].getDis():
                        self.finalPath[0].setUpPath(True)
                        self.finalPath = [self.grid[self.finalPath[0].getRow()-1][self.finalPath[0].getCol()]] + self.finalPath
                        continue
                    else:
                        self.finalPath[0].setUpPath(False)
                else:
                    self.finalPath[0].setUpPath(False)

            elif self.finalPath[0].getRightPath() == None:
                if self.checkRight(self.finalPath[0].getCol(), col-1):
                    if self.grid[self.finalPath[0].getRow()][self.finalPath[0].getCol()+1].getDis() > self.finalPath[0].getDis():
                        self.finalPath[0].setRightPath(True)
                        self.finalPath = [self.grid[self.finalPath[0].getRow()][self.finalPath[0].getCol()+1]] + self.finalPath
                        continue
                    else:
                        self.finalPath[0].setRightPath(False)
                else:
                    self.finalPath[0].setRightPath(False)

            elif self.finalPath[0].getDownPath() == None:
                if self.checkBottom(self.finalPath[0].getRow(), row-1):
                    if self.grid[self.finalPath[0].getRow()+1][self.finalPath[0].getCol()].getDis() > self.finalPath[0].getDis():
                        self.finalPath[0].setDownPath(True)
                        self.finalPath = [self.grid[self.finalPath[0].getRow()+1][self.finalPath[0].getCol()]] + self.finalPath
                        continue
                    else:
                        self.finalPath[0].setDownPath(False)
                else:
                    self.finalPath[0].setDownPath(False)

            elif self.finalPath[0].getLeftPath() == None:
                if self.checkLeft(self.finalPath[0].getCol(), 0):
                    if self.grid[self.finalPath[0].getRow()][self.finalPath[0].getCol()-1].getDis() > self.finalPath[0].getDis():
                        self.finalPath[0].setLeftPath(True)
                        self.finalPath = [self.grid[self.finalPath[0].getRow()][self.finalPath[0].getCol()-1]] + self.finalPath
                        continue
                    else:
                        self.finalPath[0].setLeftPath(False)
                else:
                    self.finalPath[0].setLeftPath(False)
            
            if self.finalPath[0].getUpPath() != None and self.finalPath[0].getDownPath() != None and self.finalPath[0].getLeftPath() != None and self.finalPath[0].getRightPath() != None:
                self.finalPath.remove(self.finalPath[0])

        

    def dijkstra(self):

        self.visited = [self.grid[self.startRow][self.startCol]]
        nextLocations = []


        for currentLoc in self.visited:
            if self.checkRight(currentLoc.getCol(), self.col-1):
                if self.grid[currentLoc.getRow()][currentLoc.getCol()+1].getVisited() == False and self.grid[currentLoc.getRow()][currentLoc.getCol()+1].getWall() == False: 
                    if self.grid[currentLoc.getRow()][currentLoc.getCol()+1].getWeight() == currentLoc.getDisRight():
                        if self.checkEnd(self.grid[currentLoc.getRow()][currentLoc.getCol()+1].getRow(), self.grid[currentLoc.getRow()][currentLoc.getCol()+1].getCol(), self.endRow, self.endCol):
                            self.endLoc.setDis(currentLoc.getDis() + self.endLoc.getWeight())
                            self.grid[self.endLoc.getRow()][self.endLoc.getCol()].setDis(self.endLoc.getDis())
                            return ("The shortest distance from row {x} column {y} to row {a} column {b} is {dis}.".format(x = self.startRow, y= self.startCol, a = self.endRow, b = self.endCol, dis = self.endLoc.getDis() ))
                        else:
                            self.grid[currentLoc.getRow()][currentLoc.getCol()+1].setDis(currentLoc.getDis() + self.grid[currentLoc.getRow()][currentLoc.getCol()+1].getWeight())
                            self.grid[currentLoc.getRow()][currentLoc.getCol()+1].setVisited(True)
                            nextLocations.append(self.grid[currentLoc.getRow()][currentLoc.getCol()+1])
                    else:
                        currentLoc.setDisRight(currentLoc.getDisRight() + 1)
                        nextLocations.append(currentLoc)
            
            if self.checkTop(currentLoc.getRow(), 0) :
                if self.grid[currentLoc.getRow()-1][currentLoc.getCol()].getVisited() == False and self.grid[currentLoc.getRow()-1][currentLoc.getCol()].getWall() == False:
                    if self.grid[currentLoc.getRow()-1][currentLoc.getCol()].getWeight() == currentLoc.getDisUp():
                        if self.checkEnd(self.grid[currentLoc.getRow()-1][currentLoc.getCol()].getRow(), self.grid[currentLoc.getRow()-1][currentLoc.getCol()].getCol(), self.endRow, self.endCol):
                            self.endLoc.setDis(currentLoc.getDis() + self.endLoc.getWeight())
                            self.grid[self.endLoc.getRow()][self.endLoc.getCol()].setDis(self.endLoc.getDis())
                            return ("The shortest distance from row {x} column {y} to row {a} column {b} is {dis}.".format(x = self.startRow, y= self.startCol, a = self.endRow, b = self.endCol, dis = self.endLoc.getDis() ))
                        else:
                            self.grid[currentLoc.getRow()-1][currentLoc.getCol()].setDis(currentLoc.getDis() + self.grid[currentLoc.getRow()-1][currentLoc.getCol()].getWeight())
                            self.grid[currentLoc.getRow()-1][currentLoc.getCol()].setVisited(True)
                            nextLocations.append(self.grid[currentLoc.getRow()-1][currentLoc.getCol()])
                    else:
                        currentLoc.setDisUp(currentLoc.getDisUp() + 1)
                        nextLocations.append(currentLoc)

            if self.checkLeft(currentLoc.getCol(), 0):
                if self.grid[currentLoc.getRow()][currentLoc.getCol()-1].getVisited() == False and self.grid[currentLoc.getRow()][currentLoc.getCol()-1].getWall() == False:
                    if self.grid[currentLoc.getRow()][currentLoc.getCol()-1].getWeight() == currentLoc.getDisLeft():
                        if self.checkEnd(self.grid[currentLoc.getRow()][currentLoc.getCol()-1].getRow(), self.grid[currentLoc.getRow()][currentLoc.getCol()-1].getCol(), self.endRow, self.endCol):
                            self.endLoc.setDis(currentLoc.getDis() + self.endLoc.getWeight())
                            self.grid[self.endLoc.getRow()][self.endLoc.getCol()].setDis(self.endLoc.getDis())
                            return ("The shortest distance from row {x} column {y} to row {a} column {b} is {dis}.".format(x = self.startRow, y= self.startCol, a = self.endRow, b = self.endCol, dis = self.endLoc.getDis() ))
                        else:
                            self.grid[currentLoc.getRow()][currentLoc.getCol()-1].setDis(currentLoc.getDis() + self.grid[currentLoc.getRow()][currentLoc.getCol()-1].getWeight())
                            self.grid[currentLoc.getRow()][currentLoc.getCol()-1].setVisited(True)
                            nextLocations.append(self.grid[currentLoc.getRow()][currentLoc.getCol()-1])
                    else:
                        currentLoc.setDisLeft(currentLoc.getDisLeft() + 1)
                        nextLocations.append(currentLoc)
            
            if self.checkBottom(currentLoc.getRow(), self.row-1): 
                if self.grid[currentLoc.getRow()+1][currentLoc.getCol()].getVisited() == False and self.grid[currentLoc.getRow()+1][currentLoc.getCol()].getWall() == False:
                    if self.grid[currentLoc.getRow()+1][currentLoc.getCol()].getWeight() == currentLoc.getDisDown():
                        if self.checkEnd(self.grid[currentLoc.getRow()+1][currentLoc.getCol()].getRow(), self.grid[currentLoc.getRow()+1][currentLoc.getCol()].getCol(), self.endRow, self.endCol):
                            self.endLoc.setDis(currentLoc.getDis() + self.endLoc.getWeight())
                            self.grid[self.endLoc.getRow()][self.endLoc.getCol()].setDis(self.endLoc.getDis())
                            return ("The shortest distance from row {x} column {y} to row {a} column {b} is {dis}.".format(x = self.startRow, y= self.startCol, a = self.endRow, b = self.endCol, dis = self.endLoc.getDis() ))
                        else:
                            self.grid[currentLoc.getRow()+1][currentLoc.getCol()].setDis(currentLoc.getDis() + self.grid[currentLoc.getRow()+1][currentLoc.getCol()].getWeight())
                            self.grid[currentLoc.getRow()+1][currentLoc.getCol()].setVisited(True)
                            nextLocations.append(self.grid[currentLoc.getRow()+1][currentLoc.getCol()])
                    else:
                        currentLoc.setDisDown(currentLoc.getDisDown() + 1)
                        nextLocations.append(currentLoc)
            
            self.visited.extend(nextLocations)
            nextLocations = []

        return "There is no possible path"

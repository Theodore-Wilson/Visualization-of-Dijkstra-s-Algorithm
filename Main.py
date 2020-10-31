import pygame
import sys

#Node class
class Node():

    #Constructor method
    def __init__(self, r, c):
        self.row = r
        self.col = c
        self.visited = False
        self.wall = False
        self.weight = 1
        self.disFromStart = sys.maxsize
        self.disUp = 1
        self.disRight = 1
        self.disDown = 1
        self.disLeft = 1
        self.upPath = None
        self.rightPath = None
        self.downPath = None
        self.leftPath = None

    #Getter and Setter Methods for all Node Class variables
    def getRow(self):
        return self.row
    
    def getCol(self):
        return self.col
    
    def getVisited(self):
        return self.visited
    
    def setVisited(self, value):
        self.visited = value

    def getWall(self):
        return self.wall

    def setWall(self, value):
        self.wall = value
    
    def getWeight(self):
        return self.weight
    
    def setWeight(self, value):
        self.weight = value
    
    def getDis(self):
        return self.disFromStart
    
    def setDis(self, value):
        self.disFromStart = value
    
    def getDisUp(self):
        return self.disUp
    
    def setDisUp(self, value):
        self.disUp = value
    
    def getDisRight(self):
        return self.disRight
    
    def setDisRight(self, value):
        self.disRight = value
    
    def getDisDown(self):
        return self.disDown
    
    def setDisDown(self, value):
        self.disDown = value
    
    def getDisLeft(self):
        return self.disLeft
    
    def setDisLeft(self, value):
        self.disLeft = value
    
    def getUpPath(self):
        return self.upPath

    def setUpPath(self, value):
        self.upPath = value
    
    def getRightPath(self):
        return self.rightPath
    
    def setRightPath(self, value):
        self.rightPath = value
    
    def getDownPath(self):
        return self.downPath
    
    def setDownPath(self, value):
        self.downPath = value
    
    def getLeftPath(self):
        return self.leftPath
    
    def setLeftPath(self, value):
        self.leftPath = value

#Dijkstras Class that has the functions to determine the shortest path
class testDijkstra():

    #Constructor Method that sets the vairbales for the Dijkstra class
    def __init__(self, r, c, sR, sC, eR, eC):
        self.row = r
        self.col = c
        self.startRow = sR
        self.startCol = sC
        self.endRow = eR
        self.endCol = eC
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

    #Helper check methods used in the Dijkstra's Algorithm Methods to ensure that I am not testing nodes not in the array
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

    #Helper check method to determine if the current Node is the end Node.
    def checkEnd(self, currentRow, currentCol, finishRow, finishCol):
        if currentRow == finishRow and currentCol == finishCol:
            return True
        return False

    #Sets walls based on user input
    def setWalls(self, r, c, val):
        self.grid[r][c].setWall(val)

    #Sets weighted Nodes based on user input
    def setWeights(self, r, c, val):
        self.grid[r][c].setWeight(val)

    #Creates a grid based on user input and sets the Start and End Nodes in the grid,
    def createGrid(self):
        self.startLoc = Node(self.startRow, self.startCol)
        self.endLoc = Node(self.endRow, self.endCol)
        self.grid = [[Node(j, i) for i in range(self.col)] for j in range(self.row)]
        self.grid[self.startRow][self.startCol].setVisited(True)
        self.grid[self.startRow][self.startCol].setDis(0)


    #Returns a list of the Nodes Visited to get the Shortest Path. Used to draw the shortest path in the Visualization.
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

        
    #Dijkstra's Path Algorithm that determines the distance to the Nodes leading to the End Node.
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

#User input for the grid including size, Start Node location, and End Node location
print ("Input your values for the grid here.")
row = int(input('How many rows: '))
col = int(input('How many columns: '))
startRow = int(input("Where would you like to Start Node Row: "))
startCol = int(input("Where would you like to Start Node Col: "))
endRow = int(input("Where would you like to End Node Row: "))
endCol = int(input("Where would you like to End Node Col: "))

#creates an instance of Dijkstra's Algorithm
d = testDijkstra(row, col, startRow, startCol, endRow, endCol)

#Creates Grid
d.createGrid()

#Stores the Grid in a temp array so it can be drawn
tempArr = d.getGrid()

#Creates the walls the user inputs
numWalls = int(input("How many walls would you like on the grid: "))
counter = 0
while (counter < numWalls):
    wallR = int(input("What row would you like for wall {num}: ".format(num = counter+1)))
    wallC = int(input("What column would you like for wall {num}: ".format(num = counter+1)))
    if wallR >= row:
        print ("That row is not within range of the grid.")
    elif wallC >= col:
        print ("That column is not within range of the grid.")
    elif tempArr[wallR][wallC].getWall() == False:
        d.setWalls(wallR, wallC, True)
        counter +=1
    elif tempArr[wallR][wallC]:
        check = input("This Node is already a wall. Do you want to change back to no wall (y = yes): ")
        if check == "y":
            d.setWalls(wallR, wallC, False)
            counter -=1
        else:        
            print ("That Node is already a wall.")

#Creates the walls the user inputs
numWeights = int(input("How many wieghted Nodes would you like on the grid: "))
counter = 0
while (counter < numWeights):
    weightR = int(input("What row would you like for weighted Node {num}: ".format(num = counter+1)))
    weightC = int(input("What column would you like for weighted Node {num}: ".format(num = counter+1)))
    weightV = int(input("What weight would you like for this weighted Node (1 is standard): "))
    if weightR >= row:
        print ("That row is not within range of the grid.")
    elif weightC >= col:
        print ("That column is not within range of the grid.")
    elif weightV <= 0:
        print ("Weight has to bee greater then 0.")
    elif tempArr[weightR][weightC].getWeight() >= 1:
        if tempArr[weightR][weightC].getWeight() > 1:
            if weightV == 1:
                check = input("This Node is already weighted. Do you want to change it to the original weight (y = yes): ")
                if check == "y":
                    d.setWeights(weightR, weightC, weightV)
                    counter -=1
                else:
                    print("That Node is already weighted.")
            else:
                check = input("This Node is already weighted. Do you want to change it to this new weight (y = yes): ")
                if check == "y":
                    d.setWeights(weightR, weightC, weightV)
                    counter +=1
        else:
            if weightV == 1:
                print ("This already has a weight of 1")
            else:
                d.setWeights(weightR, weightC, weightV)
                counter +=1

#starts pygame
pygame.init()

#Vairables used throught the Pygame to do tasks such as drawing or mouse movement
isDone = False
width = 20
height = 20
margin = 1
display_width = (width*col) + (col+1)
display_height = (height*row) + (row+1)+40
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Dijkstra's Algorithm")
clock = pygame.time.Clock()#sets Fps

while not isDone:

    for event in pygame.event.get(): #checks for what is happening in the game
        #Checks if X is clicked. If is quits Pygame
        if event.type == pygame.QUIT:
            isDone = True
    
    #Colours the background grey
    gameDisplay.fill((220,220,220))

    #Draws the button that is clicked to start the visualization
    pygame.draw.rect(gameDisplay, (0,128,0), [(display_width - 50)//2, 5, 50, 30])

    #Stores the Grid in a temp array so it can be drawn
    tempArr = d.getGrid()

    #draws base grid
    for j in range(row):
        for i in range (col):
            if j == d.getStartRow() and i == d.getStartCol():
                pygame.draw.rect(gameDisplay, (0,128,0), [margin + ((width+margin)*i), margin + ((height+margin)*j)+40, width, height])
            elif j == d.getEndRow() and i == d.getEndCol():
                pygame.draw.rect(gameDisplay, (225, 0,0), [margin + ((width+margin)*i), margin + ((height+margin)*j)+40, width, height])
            elif tempArr[j][i].getWall():
                pygame.draw.rect(gameDisplay, (0,0,0), [margin + ((width+margin)*i), margin + ((height+margin)*j)+40, width, height])
            elif tempArr[j][i].getWeight() > 1:
                pygame.draw.rect(gameDisplay, (128,0,128), [margin + ((width+margin)*i), margin + ((height+margin)*j)+40, width, height])
            else:
                pygame.draw.rect(gameDisplay, (169,169,169), [margin + ((width+margin)*i), margin + ((height+margin)*j)+40, width, height])
    
    pygame.display.update()

    #Checks if the mouse button 1 is being clicked.
    if pygame.mouse.get_pressed()[0] == 1:
        mouse = pygame.mouse.get_pos()
        #Checks if mouse is on the start button.
        if mouse[1] > 5 and mouse[1] < 35 and mouse[0] > (display_width - 50)//2 and mouse[0] < (display_width - 50)//2 +50:
            #runs the algorith
            d.dijkstra()

            #stores the order of which the Nodes were visited in a temp Array.
            tempArr = d.getVisited()

            #Draws out the order in which the Nodes were visited to demonstrate the search mecanism
            for i in range(1, len(tempArr)):
                pygame.time.delay(20)
                pygame.draw.rect(gameDisplay, (0,0, 255), [margin + ((width+margin)*tempArr[i].getCol()), margin + ((height+margin)*tempArr[i].getRow())+40, width, height])
                pygame.display.update()

            #Finds the Shortest Path
            d.shortestPath()

            #Stores the array of Nodes containing the shortest path in a temp Array.
            tempArr = d.getFinalPath()

            #Draws out the shortest parth.
            for i in range(len(tempArr)-2, 0, -1):
                pygame.time.delay(25)
                pygame.draw.rect(gameDisplay, (255, 255, 0), [margin + ((width+margin)*tempArr[i].getCol()), margin + ((height+margin)*tempArr[i].getRow())+40, width, height])
                pygame.display.update()

            #Delay on drawing so that yuou can see the search
            pygame.time.delay(6000)
            pygame.display.update()

            #Sets fps to 60
            clock.tick(60)
            #isDone = True

#Ends Pygame
pygame.quit()
quit()
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
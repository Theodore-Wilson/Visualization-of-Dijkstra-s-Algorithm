import pygame

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
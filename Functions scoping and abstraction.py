# CPRG-216
# Assignment: Function, Scoping, and Abstraction
# Group: Anton, Ethan, Joseph
# November 25, 2022

# Units
units = "feet"

# Functions
'''Asks the user about the number of rooms to be painted, the shape of each room,
 then prints the room number, area to be painted, and the cost per room, and for all rooms'''
def computeRoomArea():
    numOfRooms = int(input("How many rooms do you want to paint? \n"))
    print("Thank you!")
    totalArea = 0
    totalGallons = 0
    totalCost = 0
    for i in range(numOfRooms):
        print(f"Room: {i + 1}")
        roomShape = int(input("Select the shape of the room: \n 1 - Rectangular \n 2 - Square"
                              "\n 3 - Custom (More or less than four walls. All walls square or rectangular.) \n"))
        if roomShape == 1:
            print(f"Room: {i + 1}")
            roomArea = computeRectangleArea(rlength=int(input(f"Enter the length of the room in {units}: \n")),
                                            rwidth=int(input(f"Enter the width of the room in {units}: \n")),
                                            rheight=int(input(f"Enter the height of the room in {units}: \n"))) - computeWindowsDoorsArea()
            print(f"For room {i + 1}, the area to be painted is", roomArea,
                  f"square {units}, which will require {round(computeGallons(roomArea), 2)} gallons to paint."
                  f"\nThis will cost the customer $", round(computePaintPrice(roomArea), 2))
            totalArea += roomArea
            totalGallons += computeGallons(roomArea)
            totalCost += computePaintPrice(roomArea)
        elif roomShape == 2:
            print(f"Room: {i + 1}")
            roomArea = computeSquareWallsArea() - computeWindowsDoorsArea()
            print(f"For room {i + 1}, the area to be painted is", roomArea,
                  f"square {units}, which will require {round(computeGallons(roomArea), 2)} gallons to paint."
                  f"\nThis will cost the customer $", round(computePaintPrice(roomArea), 2))
            totalArea += roomArea
            totalGallons += computeGallons(roomArea)
            totalCost += computePaintPrice(roomArea)
        elif roomShape == 3:
            print(f"Room: {i + 1}")
            roomArea = computeCustomWallsArea() - computeWindowsDoorsArea()
            print(f"For room {i + 1}, the area to be painted is", roomArea,
                  f"square {units}, which will require {round(computeGallons(roomArea), 2)} gallons to paint."
                  f"\nThis will cost the customer $", round(computePaintPrice(roomArea), 2))
            totalArea += roomArea
            totalGallons += computeGallons(roomArea)
            totalCost += computePaintPrice(roomArea)
            print(f"Area to be painted is {totalArea} square {units}, which will require {round(totalGallons, 2)} gallons to paint. \n"
                  f"This will cost the customer ${round(totalCost, 2)}.")
            break
        else:
            print("Error, invalid input")
            break


# Takes the length and width of a rectangle and returns the value of its area
def computeRectangleArea(rlength, rwidth, rheight):
    rectangleArea = (2 * rlength * rheight) + (2 * rwidth * rheight)
    return rectangleArea


# Asks the user to enter the length, width, and height and calculates the surface area to be painted in the room
def computeRectangleWallsArea():
    rlength = int(input(f"Enter the length of the room in {units}: \n"))
    rwidth = int(input(f"Enter the width of the room in {units}: \n"))
    rheight = int(input(f"Enter the height of the room in {units}: \n"))
    rectangleWallsArea = computeRectangleArea(rlength, rwidth, rheight) - computeWindowsDoorsArea()
    return rectangleWallsArea


# Takes the side length of a square and returns the value of its area
def computeSquareArea(slength):
    squareArea = (slength * slength)
    return squareArea


# Asks the user to enter the side length of one wall side and calculates the surface area of the walls in the room
def computeSquareWallsArea():
    slength = int(input(f"Enter the length of one side of the room in {units}: \n"))
    squareWallsArea = 4 * computeSquareArea(slength)
    return squareWallsArea


# Asks the user about the number of windows or doors in a room and calculates its area for every door or window
def computeWindowsDoorsArea():
    numOfWindowsDoors = int(input("How many windows and doors does the room contain? \n"))
    windowsDoorsArea = 0
    for i in range(numOfWindowsDoors):
        wdlength = int(input(f"Enter window/door length for window/door {i + 1} in {units}: \n"))
        wdwidth = int(input(f"Enter window/door width for window/door {i + 1} in {units}: \n"))
        windowsDoorsArea += (wdlength * wdwidth)
    return windowsDoorsArea


# Asks the user to specify the number of walls in that room and calculates the room area
def computeCustomWallsArea():
    numOfWalls = int(input("How many walls are there in the room? \n"))
    customWallsArea = 0
    for i in range(numOfWalls):
        cheight = int(input(f"Enter the height of wall {i + 1} in {units}: \n"))
        cwidth = int(input(f"Enter the width of wall {i + 1} in {units}: \n"))
        customWallsArea += (cheight * cwidth)
    return customWallsArea


# Takes the area of the room as a parameter and returns the number of gallons of paint needed
def computeGallons(roomArea):
    gallonsOfPaint = float((roomArea / 350))
    return gallonsOfPaint


# Takes the area of the room as a parameter and returns the price of the gallons of paint needed
def computePaintPrice(roomArea):
    paintPrice = float((roomArea / 350) * 42)
    return paintPrice

# Program
print("Welcome to Shiny Paint Company for indoor painting!")
computeRoomArea()
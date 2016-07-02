import os.path
import sys
import input

# Check if input file exists
if not os.path.isfile('input.txt'):
    sys.exit("input.txt file does not exist.")
# Read grid graph from input.txt using input module
try :
    (W, SP) = input.file_to_grid('input.txt')
except:
    sys.exit("Error happened in reading from input.txt")

# Check if the point is a border point
def isBorderPoint(point):
    for i in range(0, 4):
        if point[i] == 3:
            return True
    return False

# Check if the point has been seen
def isPointSeen(point):
    if point[4] == 1:
        return True
    return False

# Get the point of the next neighbor
def getNeighborPoint(point, dir):
    neighborPoint = point[:]
    # Left
    if dir == 0:
        neighborPoint[1] -= 1
    # Right
    elif dir == 1:
        neighborPoint[1] += 1
    # Up
    elif dir == 2:
        neighborPoint[0] -= 1
    # Down (dir == 3)
    else:
        neighborPoint[0] += 1
    return neighborPoint

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

# Complete the path to border from the startPint and using pathsToHere
def findPath(pathsToHere, startPoint):
    pointInfo = W[startPoint[0]][startPoint[1]]

    # Check if current point exists in another found path
    if isPointSeen(pointInfo):
        # There is no path from current point to borders
        return None

    # Mark this node as seen
    pointInfo[4] = 1
    # Check if the current point is a border point
    if isBorderPoint(pointInfo):
        # Add current point to the path
        pathsToHere.append(startPoint)
        # Return the completed path
        return pathsToHere

    # Traverse every four direction of the node
    for dir in range(0, 4):
        # If the direction has no edge
        if pointInfo[dir] == 0:
            continue
        # Add current point to path
        pathWithCurrent = pathsToHere[:]
        pathWithCurrent.append(startPoint)
        # Find a path from this direction
        foundPath = findPath(pathWithCurrent, getNeighborPoint(startPoint, dir))
        # If there is a path from this direction
        if foundPath != None:
            return foundPath
    # Mark this node as not seen, because no path found
    pointInfo[4] = 0
    # No path found
    return None

# All found paths
paths = []
# For every starting point
for p in SP:
    # Find a escape path from the starting point
    path = findPath([], p)
    # If there is an escape path
    if path != None:
        paths.append(path)

# If any escape path found
if len(paths) != 0:
    print(str(len(paths)) + " paths found:")
    # Print all paths
    for path in paths:
        print("\t " + str(path))
# If no escape path found
else:
    print("No path found.")
    # Exit the program successfully
    sys.exit(0)


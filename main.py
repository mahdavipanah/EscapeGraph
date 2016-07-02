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



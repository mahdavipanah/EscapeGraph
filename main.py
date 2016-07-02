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
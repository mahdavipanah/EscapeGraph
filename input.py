from os import linesep
import re

# Reads a grid information from a file
def file_to_grid(filename):
    # Grid adjacency matrix
    W = []
    # List of starting points
    SP = []
    with open(filename) as input_file:
        # Number of columns and rows
        n = int(input_file.readline())

        # Read all rows and columns
        for i in range(0, n):
            line = input_file.readline()
            # Remove \n from end of line
            line = line.rstrip(linesep)
            # Split line into it's columns
            line = line.split(' ')
            # Split each node directions
            line = [[i[0], i[1], i[2], i[3]] for i in line]
            W.append(line)

        # Regex pattern for excluding white spaces
        pattern = re.compile(r'\s+')
        # Read all starting points
        for line in input_file:
            # Check if line is empty
            if re.sub(pattern, '', line) == '':
                # Stop reading from input file
                break
            else:
                SP.append(line.rstrip(linesep).split(' '))
    # Convert chars in W to int
    W = [[[int(n) for n in column]for column in row] for row in W]

    # Append a item to list and return the list
    def apnd(lst, item):
        lst.append(item)
        return lst
    # Adds a fifth item in every node which indicates whether that node has been seen or not
    W = [[apnd(column, 0) for column in row] for row in W]

    # Convert chars in SP to int
    SP = [[int(i) for i in p]for p in SP]
    return (W, SP)

#!/Users/anthonyquivers/anaconda3/bin/python
#Date Started: 190718


import math
import os
import random
import re
import sys

# Complete the minimumMoves function below.
def minimumMoves(grid, startX, startY, goalX, goalY):
    for row in grid:
        print(row)
    print(grid[0][1])
    return 1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    startXStartY = input().split()

    startX = int(startXStartY[0])

    startY = int(startXStartY[1])

    goalX = int(startXStartY[2])

    goalY = int(startXStartY[3])

    result = minimumMoves(grid, startX, startY, goalX, goalY)

    fptr.write(str(result) + '\n')

    fptr.close()


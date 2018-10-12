#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the cavityMap function below.
def cavityMap(grid):
    if len(grid) < 3:
        return grid
    gridRes = [grid[0]]
    for y in range(1, len(grid) - 1):
        rowCavities = []
        for x in range(1, len(grid[y]) - 1):
            curr = int(grid[y][x])
            left = int(grid[y][x - 1])
            right = int(grid[y][x + 1])
            top = int(grid[y - 1][x])
            bottom = int(grid[y + 1][x])
            if curr > left and curr > right and curr > top and curr > bottom:
                rowCavities.append(x)

        row = grid[y]
        for x in rowCavities:        
            row = row[:x] + 'X' + row[x + 1:]
        gridRes.append(row)
    gridRes.append(grid[-1])
    return gridRes

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    result = cavityMap(grid)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()

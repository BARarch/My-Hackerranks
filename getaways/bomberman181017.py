#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the bomberMan function below.
def left_right(row):
    return  row ^ ((row << 1) | 2 ^ len(row)) ^ (row >> 1)

def bomberMan(n, grid):
    ## I can use big numbers, really big numbers
    ## Lets use really big numbers
    return ["O"]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    rcn = input().split()

    r = int(rcn[0])

    c = int(rcn[1])

    n = int(rcn[2])

    grid = []

    for _ in range(r):
        grid_item = input()
        grid.append(grid_item)

    result = bomberMan(n, grid)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()

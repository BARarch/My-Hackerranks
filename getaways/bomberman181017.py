#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the bomberMan function below.
def encode(grid):
    val = 0
    for row in grid:
        for c in row
            val = val << 1
            if c == 'O':
                val += 1
    return val

def decode(val, r, c):
    grid = []
    col = 0
    row = ''
    for digit in bin(val)[2:]:
        row += digit
        col += 1
        if col == c:
            grid.append(row)
            row = ''
            col = 0
    return grid

def full_mask(r, c):
    pass

def left_mask(r, c):
    pass

def right_mask(r, c):
    pass

def make_explode(r, c):
    ## Composes the explode function exclusivly for grids
    ## with r rows and c columns
    pass


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

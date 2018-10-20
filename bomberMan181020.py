#!/bin/python3

import math
import os
import random
import re
import sys

def encode(grid):
    val = 0
    for row in grid:
        for c in row:
            val <<= 1
            if c == 'O':
                val |= 1
    return val

def decode(val, r, c):
    grid = []
    col = 0
    row = ''
    binVal = bin(val)[2:]
    binVal = ('0' * ((r * c) - len(binVal))) + binVal
    #print(binVal)
    #print(len(binVal))
    for digit in binVal:
        if digit == "0":
            row += '.'
        elif digit == '1':
            row += 'O'
        col += 1
        if col == c:
            grid.append(row)
            row = ''
            col = 0
    return grid

def print_grid(grid):
    for row in grid:
        print(row)

def print_val(val, r, c):
    for row in decode(val, r, c):
        print(row)

def full_mask(r, c):
    ## Need a number with r * c ones
    return (2 ** (r * c)) - 1 


def left_mask(r, c):
    ## Have c columns, need a number with c - 1 ones then one 0
    base = ((2 ** (c - 1)) - 1) << 1
    mask = 0
    for _ in range(r):
        mask <<= c
        mask |= base
    return mask


def right_mask(r, c):
    ## Have c columns, need a number with c - 1 ones
    base = ((2 ** (c - 1)) - 1)
    mask = 0
    for _ in range(r):
        mask <<= c
        mask |= base
    return mask


def make_explode(r, c):
    ## Composes the explode function exclusivly for grids
    ## with r rows and c columns
    leftMask = left_mask(r, c)
    rightMask = right_mask(r, c)
    fullMask = full_mask(r, c)
    def explodeFunc(reg):
        a = (reg | ((reg << 1) & leftMask)) | ((reg >> 1) & rightMask)
        b = (reg | ((reg << c) & fullMask)) | (reg >> c)
        return a | b
    return explodeFunc


def bomberMan(n, grid):
    ## I can use big numbers, really big numbers
    ## Lets use really big numbers
    r = len(grid)
    c = len(grid[0])
    fullMask = full_mask(r, c)
    explode = make_explode(r, c)
    B = encode(grid)

    if (n % 2) == 0:
        return decode(fullMask, r, c)
    if n == 0 or n == 1:
        return grid

    if (n % 4) == 3:
        A = fullMask - (B | explode(B))
        return decode(A, r, c)

    if (n % 4) == 1:
        A = fullMask - (B | explode(B))
        B = fullMask - (A | explode(A))
        return decode(B, r, c)

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

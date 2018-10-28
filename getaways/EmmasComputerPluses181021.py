#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import *

class TestCase:
    def __init__(self, fileName):
        f = open(fileName, 'r')
        st = list(map(int, f.readline().rstrip().split(' ')))
        self.r = st[0]
        self.c = st[1]
        self.grid = []

        for _ in range(self.r):
            self.grid.append(f.readline().rstrip())

        f.close()

    def get_r(self):
        return self.r

    def get_c(self):
        return self.c

    def get_grid(self):
        return self.grid

def encode(grid):
    val = 0
    for row in grid:
        for c in row:
            val <<= 1
            if c == "G":
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
    for start in range(0, len(binVal), c):
        grid.append(binVal[start:start + c])
    return grid

def full_mask(r, c):
    ## Need a number with r * c ones
    return (2 ** (r * c)) - 1

def left_mask(r, c, n):
    ## r rows of c - n 1s followed buy n 0s
    if n >= c:
        return 0
    val = 0    
    num = ((2 ** (c - n)) - 1) << n
    for _ in range(r):
        val <<= c
        val |= num
    return val

def right_mask(r, c, n):
    ## r rows of n 0s followed bu c - n 1s
    if n >= c:
        return 0
    val = 0
    num = (2 ** (c - n)) - 1
    for _ in range(r):
        val <<= c
        val |= num
    return val

def shift_left(val, r, c, n):
    if n >= c:
        return 0
    return (val << n) & left_mask(r, c, n)

def shift_right(val, r, c, n):
    if n >= c:
        return 0
    return (val >> n) & right_mask(r, c, n)

def shift_up(val, r, c, n, fullMask):
    return val << (n * c) & fullMask

def shift_down(val, r, c, n, fullMask):
    return val >> (n * c)

def print_grid(grid):
    for row in grid:
        print(row)

def crossProduct(elm):
    return elm[0] * elm[1]

def make_cross(val, r, c, n, fullMask):
    cross = val
    print('in n = {}'.format(str(n)))
    print_grid(decode(cross, r, c))
    for dist in range(1, n + 1):
        cross |= shift_down(val, r, c, dist, fullMask) | shift_left(val, r, c, dist) | shift_up(val, r, c, dist, fullMask) | shift_right(val, r, c, dist)
    print('out')
    print_grid(decode(cross, r, c))
    print()
    return cross

# Complete the twoPluses function below.
def twoPluses(grid):
    # Step 1:Encoding
    r = len(grid)
    c = len(grid[0])
    val_0 = encode(grid)
    curr = val_0
    S = []
    S.append(curr)
    fullMask = full_mask(len(grid), len(grid[0]))
   
    # Steps 2, 3,4: H and V Shifting 
    for n in range(1,7):
        curr &= shift_down(val_0, r, c, n, fullMask) & shift_left(val_0, r, c, n) & shift_up(val_0, r, c, n, fullMask) & shift_right(val_0, r, c, n) 
        if curr == 0:
            break
        else:
            S.append(curr)

    # Step 5: Cross Parsing
    # The centers of crosses of the same size are stored under the same hash
    T_0 = {}
    size = 0
    for val in S:
        # Outerloop for crosses of different sizes
        T_0[size] = []
        n = 0
        for digit in reversed(bin(val)[2:]):
            # Inner loop parses 1s
            if digit == '1':
                T_0[size].append(1 << n)
            n += 1
        size += 1
    print('Elements in T_0: {}'.format(str(len(T_0))))
    print(T_0)

    # Step 6: Make Crosses
    T = {(1 + (4 * size)): list(map(lambda val: make_cross(val, r, c, size, fullMask), T_0[size])) for size in T_0}
    print('Elements in T: {}'.format(str(len(T))))
    print(T)

    ## Last Step: Find Highest Product that does not intercept
    for comb in sorted(combinations_with_replacement(T.keys(), 2), key=crossProduct, reverse=True):
        print(comb)
        for A in T[comb[0]]:
            for B in T[comb[1]]:
                if (A & B) == 0:
                    ## Show Result
                    print_grid(decode(A | B, r, c))
                    return crossProduct(comb)
    print("Returned Nothing")

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    result = twoPluses(grid)

    fptr.write(str(result) + '\n')

    fptr.close()

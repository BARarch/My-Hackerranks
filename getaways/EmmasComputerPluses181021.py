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

        
def crossProduct(elm):
    return elm[0] * elm[1]

# Complete the twoPluses function below.
def twoPluses(grid):
    T = {}

    ## Last Step: Find Highest Product that does not intercept
    for comb in sorted(combinations_with_replacement(T.keys(), 2), key=crossProduct, reverse=True):
        for A in T[comb[0]]:
            for B in T[comb[1]]:
                if (A & B) == 0:
                    return crossProduct(comb) 




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

#!/bin/python3

import math
import os
import random
import re
import sys

class TestCase:
    def __init__(self, fileName):
        pass

    def get_n(self):
        pass

    def get_m(self):
        pass

    def get_grid(self):
        pass

        

# Complete the twoPluses function below.
def twoPluses(grid):
    pass



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

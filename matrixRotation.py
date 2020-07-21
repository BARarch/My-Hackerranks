#!/Users/anthonyquivers/anaconda3/bin/python
#Date Started: 200721

import math
import os
import random
import re
import sys
import qtimer

# Complete the function below.
@qtimer.timeit
def matrixRotation(matrix, r):

if __name__ == '__main__':
    mnr = input().rstrip().split()

    m = int(mnr[0])

    n = int(mnr[1])

    r = int(mnr[2])

    matrix = []

    for _ in range(m):
        matrix.append(list(map(int, input().rstrip().split())))

    matrixRotation(matrix, r)

#!/Users/anthonyquivers/anaconda3/bin/python
#Date Started: 201030

import math
import os
import random
import re
import sys
import qtimer

# Complete the function below.
@qtimer.timeit
def connectedCell(matrix):

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    m = int(input())

    matrix = []

    for _ in range(n):
        matrix.append(list(map(int, input().rstrip().split())))

    result = connectedCell(matrix)

    fptr.write(str(result) + '\n')

    fptr.close()

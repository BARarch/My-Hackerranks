#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the chessboardGame function below.
def chessboardGame(x, y):
    return "Second" if (((x - 1) // 2) % 2 == 0) and (((y - 1) // 2) % 2 == 0) else "First"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        xy = input().split()

        x = int(xy[0])

        y = int(xy[1])

        result = chessboardGame(x, y)

        fptr.write(result + '\n')

    fptr.close()

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the cutTheSticks function below.
def cutTheSticks(arr):
    sticks = sorted(arr)
    cuts = []
    while sticks:
        shortest = sticks[0]
        keeps = []
        cuts.append(len(sticks))
        for i in range(1, len(sticks)):
            if sticks[i] > shortest:
                keeps.append(sticks[i] - shortest)
        sticks = keeps
    return cuts          

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()


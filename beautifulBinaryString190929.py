#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the beautifulBinaryString function below.
def beautifulBinaryString(b):
    ## for every subtring of  '010' in b count one switch for the last '0
    ## then move 3
    ## otherwise move 1
    q = 0
    flips = 0
    while q < len(b):
        if b[q:q + 3] == '010':
            flips += 1
            q += 3
        else:
            q += 1

    return flips

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    b = input()

    result = beautifulBinaryString(b)

    fptr.write(str(result) + '\n')

    fptr.close()


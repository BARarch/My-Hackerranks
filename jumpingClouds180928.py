#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    curr = 0
    jmps = 0
    while curr < (len(c) - 1):
        if (curr + 2) >= len(c) or c[curr + 2]:
            curr += 1
        else:
            curr += 2
        jmps += 1
    return jmps

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()

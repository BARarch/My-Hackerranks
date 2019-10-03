#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumAbsoluteDifference function below.
def minimumAbsoluteDifference(arr):
    prev = None
    absMin = 1000000001

    for n in sorted(arr):
        if prev is None:
            prev = n
            continue
        if abs(prev - n) < absMin:
            absMin = abs(prev - n)
        prev = n
    return absMin



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()


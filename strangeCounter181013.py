#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the strangeCounter function below.
def strangeCounter(t):
    return strangeCounterHelper(t - 1, 0, 3)
    
def strangeCounterHelper(t, i, maxx):
    if t < i + maxx:
        return maxx - (t - i)
    else:
        return strangeCounterHelper(t, i + maxx, 2 * maxx)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    result = strangeCounter(t)

    fptr.write(str(result) + '\n')

    fptr.close()

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the marsExploration function below.
def marsExploration(s):
    mark = (0, 'S')
    diff = 0
    for c in enumerate(s):
        if c[0] % 3 == 0 or c[0] % 3 == 2:
            if c[1] != 'S':
                diff += 1
        else:
            if c[1] != 'O':
                diff += 1
    return diff


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = marsExploration(s)

    fptr.write(str(result) + '\n')

    fptr.close()


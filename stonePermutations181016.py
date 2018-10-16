#!/bin/python3

import math
import os
import random
import re
import sys

from itertools import *

# Complete the stones function below.
def stones(n, a, b):
    if a == b:
        return [a * (n - 1)]
    else:
        return list(sorted(map(sum, combinations_with_replacement([a, b], n - 1))))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input())

    for T_itr in range(T):
        n = int(input())

        a = int(input())

        b = int(input())

        result = stones(n, a, b)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()

#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import *

# Complete the absolutePermutation function below.
def absolutePermutation(n, k):
    if k == 0:
        return list(range(1, n + 1))
    elif n % (2 * k) == 0:
        res = []
        pos = count(1)
        offset = cycle(chain(repeat(1, k), repeat(-1, k)))
        for _ in range(n):
            res.append(next(pos) + (k * next(offset)))
        return res  
    else:
        return [-1]
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        result = absolutePermutation(n, k)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()

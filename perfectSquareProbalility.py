#!/Users/anthonyquivers/anaconda3/bin/python
#Date Started: 201105

import math
import os
import random
import re
import sys
import qtimer
from math import sqrt, ceil
from fractions import Fraction


# Complete the function below.
def even_perfect_square(n):
    return not (sqrt(n) % 2)


@qtimer.timeit
def solve(N):
    q = 1
    p = 0
    n = sqrt(N)
    for i in range(2, ceil(n)):
        #print(f'i = {i}')
        if (N % i) == 0:
            q += 2
            if (sqrt(i) % 2) == 0:
                p += 1
            if (sqrt(N // i) % 2) == 0:
                p += 1

    if (N % n) == 0:
        q += 1
        if (sqrt(n) % 2) == 0:
            p += 1

    return str(Fraction(p, q))


def solve_bad(N):
    n = ceil(sqrt(N))
    q = 0
    p = 0
    for i in range(1, n + 1):
        if (N % i == 0):
            if N // i == i or i == 1:
                q += 1
                print(i)
                if not (sqrt(i) % 2):
                    print(f'psu: {i}')
                    p += 1
            else:
                q += 2
                print(i)
                print(N // i)
                if not (sqrt(i) % 2):
                    print(f'psa: {i}')
                    p += 1
                if not (sqrt(N // i) % 2):
                    print(f'psb: {N // i}')
                    p += 1
    return str(Fraction(p, q))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = solve(n)

        fptr.write(result + '\n')

    fptr.close()

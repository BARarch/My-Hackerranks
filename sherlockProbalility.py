#!/Users/anthonyquivers/anaconda3/bin/python
#Date Started: 201015

import math
import os
import random
import re
import sys
import qtimer

# Complete the function below.
from itertools import combinations_with_replacement
from fractions import Fraction


def print_fraction(arr, k):
    num = num_valid_pairs(arr, k)
    den = len(arr)**2  # power of 2
    if num == den:
        return "1/1"
    elif num:
        return str(Fraction(num, den))
    else:
        return "0/1"


@qtimer.timeit
def solve(n, k, s):
    return print_fraction(list(s), k)


def num_valid_pairs(S, k):
    nOneOne = 0
    for i, val in enumerate(S):
        if val == '1':
            nOneOne += 1
            j = 1
            while j <= k and (i + j) <= n - 1:
                if S[i + j] == '1':
                    nOneOne += 2
                j += 1

    return nOneOne


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        s = input()

        result = solve(n, k, s)

        fptr.write(result + '\n')

    fptr.close()

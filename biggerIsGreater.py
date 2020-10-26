#!/Users/anthonyquivers/anaconda3/bin/python
#Date Started: 201026

import math
import os
import random
import re
import sys
import qtimer

# Complete the function below.
from itertools import permutations
from collections import Counter


def greatest(s):
    return ''.join(reversed(sorted(s)))


def min_perms(s):
    return min([''.join(p) for p in permutations(s) if ''.join(p) > s])


@qtimer.timeit
def biggerIsGreater(w):
    for i in range(len(w) - 2, -1, -1):
        if w[i] < w[i + 1]:
            head = w[:i]
            pivot = min(c for c in w[i + 1:] if c > w[i])
            tail = Counter(w[i:])
            tail[pivot] -= 1
            return head + pivot + "".join(sorted(tail.elements()))
    return "no answer"


def biggerIsGreaterRTE(w):
    for i in range(-1, -len(w) - 1, -1):
        p = w[i:]
        if greatest(p) > p:
            mp = min_perms(p)
            print(mp)
            return w[:i] + mp
    print('NONE')
    return 'no answer'


@qtimer.timeit
def biggerIsGreaterBF(w):
    perms = [''.join(p) for p in permutations(w) if ''.join(p) > w]
    if perms:
        return min(perms)
    return 'no answer'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input())

    for T_itr in range(T):
        w = input()

        result = biggerIsGreater(w)

        #fptr.write(result + '\n')

    fptr.close()

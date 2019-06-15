#!/Users/anthonyquivers/anaconda3/bin/python
#Date Started: 190608


import math
import os
import random
import re
import sys
from collections import deque

def odd(n):
    return (n % 2) == 1

# Complete the fairRations function below.
def fairRations(B):
    # With every pair of loaves given, nOdd must decrease
    # There exists a maximum number of loaves given, what is it?
    print(B)
    oddInds = deque()
    i = 1
    loves = 0
    for n in B:
        if odd(n):
            oddInds.append(i)

        i += 1

    ## Add a loaf
    while len(oddInds) > 0:
        print(oddInds)
        if len(oddInds) == 1:
            return 'NO'

        a = oddInds.popleft()
        b = oddInds.popleft()
        loves += 2

        if (a + 1) != b:
            # Move a over one position push b back too
            oddInds.appendleft(b)
            oddInds.appendleft(a + 1)

    return loves
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    N = int(input())

    B = list(map(int, input().rstrip().split()))

    result = fairRations(B)

    fptr.write(str(result) + '\n')

    fptr.close()

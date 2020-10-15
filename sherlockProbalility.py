#!/Users/anthonyquivers/anaconda3/bin/python
#Date Started: 201015

import math
import os
import random
import re
import sys
import qtimer

# Complete the function below.
@qtimer.timeit
#!/bin/python3

import os
import sys

# Complete the solve function below.
def solve(n, k, s):

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

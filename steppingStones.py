#!/Users/anthonyquivers/anaconda3/bin/python
#Date Started: 201021

import math
import os
import random
import re
import sys
import qtimer

# Complete the function below.
@qtimer.timeit
def solve(n):

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = solve(n)

        fptr.write(result + '\n')

    fptr.close()

#!/Users/anthonyquivers/anaconda3/bin/python
#Date Started: 201111

import math
import os
import random
import re
import sys
import qtimer

# Complete the function below.
@qtimer.timeit
import os
import sys

# Complete the solve function below.
def solve(n):

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = input()

        result = solve(n)

        fptr.write(result + '\n')

    fptr.close()

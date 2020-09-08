#!/Users/anthonyquivers/anaconda3/bin/python
#Date Started: 200908

import math
import os
import random
import re
import sys
import qtimer

# Complete the function below.
@qtimer.timeit
# Complete the gameOfStones function below.
def gameOfStones(n):

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = gameOfStones(n)

        fptr.write(result + '\n')

    fptr.close()

#!/Users/anthonyquivers/anaconda3/bin/python
#Date Started: 201027

import math
import os
import random
import re
import sys
import qtimer

# Complete the function below.
@qtimer.timeit
def getMinimumCost(k, c):

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    minimumCost = getMinimumCost(k, c)

    fptr.write(str(minimumCost) + '\n')

    fptr.close()


#!/Users/anthonyquivers/anaconda3/bin/python
#Date Started: 201001

import math
import os
import random
import re
import sys
import qtimer

# Complete the function below.
@qtimer.timeit
def balancedSums(arr):

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = balancedSums(arr)

        fptr.write(result + '\n')

    fptr.close()

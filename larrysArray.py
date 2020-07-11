#!/Users/anthonyquivers/anaconda3/bin/python
#Date Started: 200711

import math
import os
import random
import re
import sys
import qtimer

# Complete the function below.
@qtimer.timeit
def larrysArray(A):

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        A = list(map(int, input().rstrip().split()))

        result = larrysArray(A)

        fptr.write(result + '\n')

    fptr.close()

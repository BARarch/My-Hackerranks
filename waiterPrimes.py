#!/Users/anthonyquivers/anaconda3/bin/python
#Date Started: 201112

import math
import os
import random
import re
import sys
import qtimer

# Complete the function below.
@qtimer.timeit
def waiter(number, q):
    #
    # Write your code here.
    #

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nq = input().split()

    n = int(nq[0])

    q = int(nq[1])

    number = list(map(int, input().rstrip().split()))

    result = waiter(number, q)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

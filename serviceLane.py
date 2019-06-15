#!/Users/anthonyquivers/anaconda3/bin/python
#Date Started: 190608

import math
import os
import random
import re
import sys

# Complete the serviceLane function below.
def serviceLane(width, cases):
    return map(lambda x:min(width[x[0]:(x[1] + 1)]), cases)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nt = input().split()

    n = int(nt[0])

    t = int(nt[1])

    width = list(map(int, input().rstrip().split()))

    cases = []

    for _ in range(t):
        cases.append(list(map(int, input().rstrip().split())))

    result = serviceLane(width, cases)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

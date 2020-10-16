#!/Users/anthonyquivers/anaconda3/bin/python
#Date Started: 201016

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

#
# Complete the runningMedian function below.
#
def runningMedian(a):
    #
    # Write your code here.
    #

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a_count = int(input())

    a = []

    for _ in range(a_count):
        a_item = int(input())
        a.append(a_item)

    result = runningMedian(a)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

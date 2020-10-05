#!/Users/anthonyquivers/anaconda3/bin/python
#Date Started: 201005

import math
import os
import random
import re
import sys
import qtimer

# Complete the function below.
@qtimer.timeit
def quickSort(arr):
    return 1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = list(map(int, input().rstrip().split()))

    result = quickSort(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

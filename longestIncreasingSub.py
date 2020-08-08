#!/Users/anthonyquivers/anaconda3/bin/python
#Date Started: 200807

import math
import os
import random
import re
import sys
import qtimer

# Complete the function below.
@qtimer.timeit
def longestIncreasingSubsequence(arr):

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr_item = int(input())
        arr.append(arr_item)

    result = longestIncreasingSubsequence(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

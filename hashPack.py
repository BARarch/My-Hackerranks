#!/Users/anthonyquivers/anaconda3/bin/python
#Date Started: 200326

#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the packNumbers function below.
def packNumbers(arr):

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = []

    for _ in range(arr_count):
        arr_item = int(input().strip())
        arr.append(arr_item)

    res = packNumbers(arr)

    fptr.write('\n'.join(res))
    fptr.write('\n')

    fptr.close()

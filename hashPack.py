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
    res = []
    prev = None
    Bundle = False
    for i in arr:
        if i == prev and not Bundle:
            N = 2
            Bundle = True
        elif i == prev and Bundle:
            N += 1
        elif Bundle:
            Bundle = False
            res.append(str(prev) + ':' + str(N))
        else:
            if prev is not None:
                res.append(str(prev))

        prev = i
    ## End States
    if Bundle:
        res.append(str(prev) + ':' + str(N))
    else:
        if prev is not None:
            res.append(str(prev))
    #print(res)
    return res

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

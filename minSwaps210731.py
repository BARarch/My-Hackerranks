#Date Started: 210731 

import math
import os
import random
import re
import sys
import qtimer

# Complete the function below.
@qtimer.timeit
def minimumSwaps(arr):
    nSwaps = 0
    for i in range(len(arr)):
        while arr[i] != (i + 1):
            #print(f'swap the {arr[arr[i] - 1]} with the {arr[i]}')
            num = arr[i]
            arr[i], arr[num - 1] = (arr[num - 1], arr[i])
            #print(arr)
            nSwaps += 1
        
    return nSwaps


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()

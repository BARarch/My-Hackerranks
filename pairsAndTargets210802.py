#Date Started: 210802 

import math
import os
import random
import re
import sys
import qtimer

# Complete the function below.
@qtimer.timeit
def pairs(k, arr):
    arr.sort()

    n = 0
    for num in arr:
        left = 0
        right = len(arr)
        #print(num)
        while left < right:
            
            mid = (right + left) // 2
            #print(f'mid = {mid}: {arr[mid]}')
            if (num - arr[mid] - k) == 0:
                n += 1
                break
            if (num - arr[mid] - k) < 0:
                right = mid
            elif left == mid:
                break
            else:
                left = mid

    return n 


def pairsSlow(k, arr):
    n = 0
    for i in arr:
        for j in arr:
            if j - i == k:
                n += 1

    return n

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = pairs(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()

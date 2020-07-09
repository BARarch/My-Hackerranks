#!/Users/anthonyquivers/anaconda3/bin/python
#Date Started: 190829

import math
import os
import random
import re
import sys

# Find the continuous subset in arr that sums to sum
def sss(arr, ssum):
    start = 0
    stop = 0
    currSum = arr[0]

    while stop < len(arr) + 1:
        if currSum == ssum:
            return (start + 1, stop + 1)

        elif currSum > ssum:
            currSum -= arr[start]
            start += 1
            continue

        else:
            if (stop + 1) < len(arr):
                stop += 1
                currSum += arr[stop]
            else:
                return (-1,)

    return (-1,)

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    N = int(input())
    for _ in range(N):
        nSum = list(map(int, input().split()))
        answer = sss(list(map(int, input().split())), nSum[1])
        print(" ".join(list(map(str, answer))))

    #fptr.close()

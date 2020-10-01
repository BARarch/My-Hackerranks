#!/Users/anthonyquivers/anaconda3/bin/python
#Date Started: 201001

import math
import os
import random
import re
import sys
import qtimer


# Complete the function below.
@qtimer.timeit
def balancedSumsGen(arr):
    def left_sum(arr):
        summ = 0
        i = 0
        for n in arr:
            yield summ, i
            summ += n
            i += 1

    def right_sum(arr):
        summ = 0
        i = len(arr) - 1
        for n in reversed(arr):
            yield summ, i
            summ += n
            i -= 1

    def index(elm):
        return elm[1]

    def locSum(elm):
        return elm[0]

    lower = left_sum(arr)
    upper = right_sum(arr)

    a = next(lower)
    b = next(upper)

    while index(a) < index(b):
        if locSum(a) < locSum(b):
            ## Step the left index
            a = next(lower)
        else:
            b = next(upper)

    if a == b:
        return "YES"
    else:
        return "NO"


@qtimer.timeit
def balancedSums(arr):
    leftSum = [0] * len(arr)
    S = 0
    for i, num in enumerate(arr):
        S += num
        if i < len(arr) - 1:
            leftSum[i + 1] = S

    rightSum = [0] * len(arr)
    S = 0
    for i, num in enumerate(reversed(arr)):
        S += num
        if i < len(arr) - 1:
            rightSum[-(i + 2)] = S

    #print(leftSum)
    #print(rightSum)

    for i, j in zip(leftSum, rightSum):
        if i == j:
            return "YES"
        if i > j:
            return "NO"

    return "NO"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = balancedSums(arr)

        fptr.write(result + '\n')

    fptr.close()

#Date Started: 210731 

import math
import os
import random
import re
import sys
import qtimer

# Complete the function below.
@qtimer.timeit
def countTriplets(arr, r):
    nTriplets = 0
    singles = {}
    pairs = {}

    for num in arr:
        if num % (r ** 2) == 0 and (num // (r ** 2), num // r) in pairs:
                nTriplets += pairs[(num // (r ** 2), num // r)]
    
        if num % r == 0 and num // r in singles:
            if (num // r, num) in pairs:
                pairs[(num // r, num)] += singles[num // r]
            else:
                pairs[(num // r, num)] = singles[num // r]
    
        if num in singles:
            singles[num] += 1
        else:
            singles[num] = 1

    return nTriplets

def countTripletsReversed(arr, r):
    nTriplets = 0
    singles = {}
    pairs = {}

    for num in arr:
        if num in singles:
            singles[num] += 1
        else:
            singles[num] = 1

        if num % r == 0 and num // r in singles:
            if (num // r, num) in pairs:
                pairs[(num // r, num)] += singles[num // r]
            else:
                pairs[(num // r, num)] = singles[num // r]

            if num % (r ** 2) == 0 and (num // (r ** 2), num // r) in pairs:
                nTriplets += pairs[(num // (r ** 2), num // r)]

    return nTriplets

def countTripletsSlow(arr, r):

    #from collections import Deque
    Ind = {}
    for i, num in enumerate(arr):
        if num in Ind:
            Ind[num].append(i)
        else:
            Ind[num] = [i, ]

    print(Ind)

    Num = {}
    for i, num in enumerate(arr):
        if num in Num:
            Num[num] += 1
        else:
            Num[num] = 1

    #pairs = Deque()
    nTriplets = 0
    for first in range(len(arr)):
        seconds = []
        if arr[first] * r in Ind:
            for second in filter(lambda sec: sec > first, Ind[arr[first] * r] ):
                seconds.append(second)
                
            if arr[first] * r * r in Ind:
                for second in seconds:
                    for third in filter(lambda rd:rd > second, Ind[arr[first] * r * r]):
                        #print((first, second, third), end=" ")
                        nTriplets += 1

    triplets = 0
    for i in range(len(arr)):
        if arr[i] * r in Num:
            n = Num[arr[i] * r][i]
            if arr[i] * r * r in Num:
                triplets += n * Num[arr[i] * r * r]

    return #nTriplets

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    ans = countTriplets(arr, r)

    fptr.write(str(ans) + '\n')

    fptr.close()

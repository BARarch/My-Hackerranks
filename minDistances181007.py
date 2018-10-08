#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumDistances function below.
def min_dists(a):
    minn = None
    for i in range(1, len(a)):
        diff = a[i] - a[i - 1]
        if not minn:
            minn = diff
        elif diff < minn:
            minn = diff
    return minn 

def minimumDistances(a):
    pos = {}
    for i in range(len(a)):
        num = a[i]
        if num in pos:
            pos[num].append(i)
        else:
            pos[num] = [i]
            
    pairDists = list(filter(lambda a: len(a) > 1, pos.values()))
    if pairDists:
        print
        return min(list(map(min_dists, pairDists)))
    else:
        return -1
    #print(pairDists)
            
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    fptr.write(str(result) + '\n')

    fptr.close()

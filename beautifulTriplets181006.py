#!/bin/python3

import math
import os
import random
import re
import sys

from itertools import combinations

# Complete the beautifulTriplets function below.
def beautifulTriplets(d, arr):
    nTriplets = 0
    i = 0
    j = 0
    k = 0
    while i < len(arr):
        js = 0
        iss = 0
        ks = 0
        if arr[k] < arr[i] + (2 * d):
            if k < len(arr) - 1:
                k += 1
            else:
                i += 1
                break           
        elif arr[k] == arr[i] + (2 * d):
            while arr[j] < arr[i] + d:
                j += 1
            ## Find Beautifult Triplets
            while arr[j] == arr[i] + d:
                ### Here is a beautifult triplet
                js += 1
                j += 1
                a = arr[i]
                b = arr[j]
                c = arr[k]
            ## No j's
            if js == 0:
                i += 1
            ## Find extra i's
            while js > 0 and a == arr[i]:
                iss += js
                i += 1
            ## Find extra k's
            while js > 0 and c == arr[k]:
                ks += iss
                if k < len(arr) - 1:
                    k += 1
                else:
                    i += 1
                    break
            ## Increment Triplets    
            nTriplets += ks
        elif arr[k] > arr[i] + (2 * d):
            i += 1
                   
    return nTriplets

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    arr = list(map(int, input().rstrip().split()))

    result = beautifulTriplets(d, arr)

    fptr.write(str(result) + '\n')

    fptr.close()

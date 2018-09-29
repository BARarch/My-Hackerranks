#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the appendAndDelete function below.
def appendAndDelete(s, t, k):
    ## unlimited k case
    if k >= (len(s) + len(t)):
        return 'Yes'
    
    if len(s) > len(t):
        ## T is shorter
        req = len(s) - len(t)
        keep = len(t)
    else:
        ## S is shorter or they are the same length
        req = len(t) - len(s)
        keep = len(s)

    ## Too few for length Case
    if req > k:
        return 'No'
    
    ## Part of string is correct even/odd k and requirements
    while s[:keep] != t[:keep]:
        req += 2
        keep -= 1
        if req > k:
            return 'No'
    if req % 2 == k % 2:
        return 'Yes'
    else:
        return 'No'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    k = int(input())

    result = appendAndDelete(s, t, k)

    fptr.write(result + '\n')

    fptr.close()

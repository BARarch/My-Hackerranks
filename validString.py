#!/Users/anthonyquivers/anaconda3/bin/python
#Date Started: 201019

import math
import os
import random
import re
import sys
import qtimer


# Complete the function below.
@qtimer.timeit
def isValid(s):
    S = {}
    V = {}

    for c in s:
        if c in S:
            S[c] += 1
        else:
            S[c] = 1

    for n in S.values():
        if n in V:
            V[n] += 1
        else:
            V[n] = 1

    #print(s)
    #print(S)
    #print(V)

    if len(V) == 1:
        return "YES"

    ## remove 1 see what happens
    singleFreq = None
    for f in V:
        if V[f] == 1:
            if singleFreq is None:
                singleFreq = f
            else:
                return "NO"

    if singleFreq:
        if (singleFreq - 1) == 0:
            del V[f]
        elif (singleFreq - 1) in V:
            V[singleFreq - 1] += 1
            del V[singleFreq]

    if len(V) == 1:
        return "YES"

    return "NO"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()

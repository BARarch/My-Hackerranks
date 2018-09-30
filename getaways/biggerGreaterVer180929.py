#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the biggerIsGreater function below.
def biggerIsGreater(w):
    ## Push partial solutions to list
    ## Sort the list
    ## For each charater, if there is a swap with any other one to its left
    ## push that solution and stop
    solns = []
    wRev = ''.join(reversed(w))
    for curr in range(len(w)):
        aft = wRev[:curr]
        rem = wRev[curr + 1:]
        incr = curr + 1
        for ch in rem:
            if ch < wRev[curr]:
                ## Perform Swap
                swap = list(aft + ch + rem)
                swap[incr] = wRev[curr]
                ## Push Soln
                solns.append(''.join(reversed(swap)))
                ## Stop
                break
            incr += 1
    if solns:
        return sorted(solns)[0]
    else:
        return 'no answer'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input())

    for T_itr in range(T):
        w = input()

        result = biggerIsGreater(w)

        fptr.write(result + '\n')

    fptr.close()

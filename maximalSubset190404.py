#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the nonDivisibleSubset function below.
def nonDivisibleSubset(k, S):
    # Its just programming

    # Step 1: Count mods
    modCounts = {}
    for num in S:
        mod = num % k
        if mod in modCounts:
            modCounts[mod] +=1
        else:
            modCounts[mod] = 1

    # Step 2: Find Conjucates and Compare
    for mod in modCounts:
        if mod == 0 or mod == (k / 2):
            # Only one of these can be in the maximal set
            modCounts[mod] = 1
        else:
            # Find Conjucate
            conj = k - mod
            if conj in modCounts:
                # Compare: Can't use numbers in both conjucate set
                # only use the numbers from the largest set
                # cancel out the number of mods from the smaller set for now
                if modCounts[mod] > modCounts[conj]:
                    modCounts[conj] = 0
                else:
                    modCounts[mod] = 0

    # Step 3: Sum up remaining mods
    return sum(modCounts.values())

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    S = list(map(int, input().rstrip().split()))

    result = nonDivisibleSubset(k, S)

    fptr.write(str(result) + '\n')

    fptr.close()    
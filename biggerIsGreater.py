#!/Users/anthonyquivers/anaconda3/bin/python
#Date Started: 191007

#!/bin/python3

import math
import os
import random
import re
import sys

def biggerIsGreater(w):
    greaterList = []
    for i, c in enumerate(reversed(w)):
        if not greaterList:
            greaterList.append(c)
        elif c >= greaterList[len(greaterList) - 1]:
            greaterList.append(c)
        else:
            for j, letter in enumerate(greaterList):
                if letter > c:
                    # Execute First Swap
                    res = w[:len(w) - i - 1] + letter
                    greaterList[j] = c
                    # Sort the rest
                    return res + ''.join(sorted(greaterList))
    return 'no answer'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input())

    for T_itr in range(T):
        w = input()

        result = biggerIsGreater(w)

        fptr.write(result + '\n')

    fptr.close()

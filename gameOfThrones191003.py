#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the gameOfThrones function below.
def gameOfThrones(s):
    gateKey = {}

    for c in s:
        if c in gateKey:
            gateKey[c] += 1
        else:
            gateKey[c] = 1

    centerKey = None
    for q in gateKey.values():   
        if  q % 2:
            if centerKey is None:
                centerKey = q
            else:
                return "NO"

    return "YES"
        


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = gameOfThrones(s)

    fptr.write(result + '\n')

    fptr.close()

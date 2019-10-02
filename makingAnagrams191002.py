#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the makingAnagrams function below.
def makingAnagrams(s1, s2):
    import string
    ss1 = {x: 0 for x in string.ascii_lowercase}
    for c in s1:
        ss1[c] += 1

    ss2 = {x: 0 for x in string.ascii_lowercase}
    for c in s2:
        ss2[c] += 1

    return sum(map(lambda x: abs(x[0] - x[1]), zip(ss1.values(), ss2.values())))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()

    s2 = input()

    result = makingAnagrams(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()

#Date Started: 210802 

import math
import os
import random
import re
import sys
import qtimer

# Complete the function below.
@qtimer.timeit
def substrCount(n, s):
    nSubstrings = 0
    for i, ch in enumerate(s):
        nSubstrings += 1
        
        prefix, j = ch, i + 1
        while j < n and s[j] == ch:
            nSubstrings += 1
            prefix += ch
            j += 1

        if s[j + 1: j + 1 + len(prefix)] == prefix:
            nSubstrings += 1

    return nSubstrings
        


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = substrCount(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()


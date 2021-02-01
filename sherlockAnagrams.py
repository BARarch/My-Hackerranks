#!/Users/anthonyquivers/anaconda3/bin/python
#Date Started: 201020

import math
import os
import random
import re
import sys
import qtimer


# Complete the function below.
def substrings(s):
    return [s[i:j] for i in range(len(s)) for j in range(i + 1, len(s) + 1)]


@qtimer.timeit
def sherlockAndAnagrams(s):
    subs = substrings(s)
    matches = {}
    for substring in substrings(s):
        sortedSubstring = ''.join(sorted(substring))
        if sortedSubstring in matches:
            matches[sortedSubstring] += 1
        else:
            matches[sortedSubstring] = 0

    nAnagrams = 0
    for nMatches in matches.values():
        nAnagrams += (((nMatches + 1)**2) - (nMatches + 1)) // 2

    return nAnagrams


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()

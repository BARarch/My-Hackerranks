#!/Users/anthonyquivers/anaconda3/bin/python
#Date Started: 191002

import math
import os
import random
import re
import sys

# Complete the palindromeIndex function below.
def palindromeIndex(s):
    remove = -1
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            if s[left + 1] == s[right]:
                remove = left
                left += 1
            elif s[left] == s[right - 1]:
                remove = right
                right -= 1
        left += 1
        right -= 1 
    return remove

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = palindromeIndex(s)

        fptr.write(str(result) + '\n')

    fptr.close()

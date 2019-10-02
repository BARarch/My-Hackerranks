#!/Users/anthonyquivers/anaconda3/bin/python
#Date Started: 191002

import math
import os
import random
import re
import sys

# Complete the palindromeIndex function below.
def palindromeIndex(s):
    def checkforpalindrome(s):
        return list(s) == list(reversed(s))
    
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            if checkforpalindrome(s[left + 1:right + 1]):
                return left
            if checkforpalindrome(s[left:right]):
                return right

        left += 1
        right -= 1
                
    return -1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = palindromeIndex(s)

        fptr.write(str(result) + '\n')

    fptr.close()

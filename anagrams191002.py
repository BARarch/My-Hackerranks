#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the anagram function below.
def anagram(s):

    if len(s) % 2 == 1:
        return -1

    import string
    s1 = {x: 0 for x in string.ascii_lowercase}
    for c in s[:len(s) // 2]:
        s1[c] += 1
    count = 0
    for c in s[len(s) // 2:]:
        if s1[c] == 0:
            count += 1
        else:
            s1[c] -= 1

    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = anagram(s)

        fptr.write(str(result) + '\n')

    fptr.close()

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the funnyString function below.
def funnyString(s):
    diff1 = []
    prev = ord(s[0])
    for c in s[1:]:
        diff1.append(abs(prev - ord(c)))
        prev = ord(c)

    diff2 = []
    s = list(reversed(s))
    prev = ord(s[0])
    for c in s[1:]:
        diff2.append(abs(prev - ord(c)))
        prev = ord(c)

    if diff1 == diff2:
        return "Funny"
    else:
        return "Not Funny"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = funnyString(s)

        fptr.write(result + '\n')

    fptr.close()


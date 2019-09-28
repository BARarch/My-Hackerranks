#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hackerrankInString function below.
def hackerrankInString(s):
    target = "hackerrank"
    #s = iter(s)
    #c = next(s)
    for hackerrankChar in target:
        if len(s) == 0:
            return "NO"
        print(s)
        for i, c in enumerate(s):
            if c == hackerrankChar:
                s = s[i + 1:]
                break
            if i == len(s) - 1:
                return "NO"
            
    return "YES"
        


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = hackerrankInString(s)

        fptr.write(result + '\n')

    fptr.close()

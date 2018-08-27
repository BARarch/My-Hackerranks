#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the alternatingCharacters function below.
def alternatingCharacters(s):
    lookA = False
    first = True
    deletions = 0
    
    for c in s:
        if first:
            if c == 'B':
                lookA = True
            first = False
        elif lookA:
            if c == 'A':
                lookA = False
            else:
                deletions +=1
        else:
            if c == 'B':
                lookA = True
            else:
                deletions += 1
                
    return deletions
                
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = alternatingCharacters(s)

        fptr.write(str(result) + '\n')

    fptr.close()

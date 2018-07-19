import math
import os
import random
import re
import sys
# Complete the solve function below.
def capitalise(w): 
    if len(w) > 0 and w[0].isalpha():
        return w[0].upper() + w[1:]
    else:
        return w

def solve(s):
    return " ".join([capitalise(w) for w in s.split(" ")])

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()

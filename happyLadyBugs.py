#!/Users/anthonyquivers/anaconda3/bin/python
#Date Started: 190618


import math
import os
import random
import re
import sys

# Complete the happyLadybugs function below.
def happyLadybugs(b):

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input())

    for g_itr in range(g):
        n = int(input())

        b = input()

        result = happyLadybugs(b)

        fptr.write(result + '\n')

    fptr.close()

#!/Users/anthonyquivers/anaconda3/bin/python
#Date Started: 190608


import math
import os
import random
import re
import sys

# Complete the fairRations function below.
def fairRations(B):

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    N = int(input())

    B = list(map(int, input().rstrip().split()))

    result = fairRations(B)

    fptr.write(str(result) + '\n')

    fptr.close()

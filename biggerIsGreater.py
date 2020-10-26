#!/Users/anthonyquivers/anaconda3/bin/python
#Date Started: 201026

import math
import os
import random
import re
import sys
import qtimer

# Complete the function below.
@qtimer.timeit
def biggerIsGreater(w):

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input())

    for T_itr in range(T):
        w = input()

        result = biggerIsGreater(w)

        fptr.write(result + '\n')

    fptr.close()

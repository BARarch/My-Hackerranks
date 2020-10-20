#!/Users/anthonyquivers/anaconda3/bin/python
#Date Started: 201020

import math
import os
import random
import re
import sys
import qtimer

# Complete the function below.
@qtimer.timeit
def sherlockAndAnagrams(s):

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()

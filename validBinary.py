#!/Users/anthonyquivers/anaconda3/bin/python
#Date Started: 200804

import math
import os
import random
import re
import sys
import qtimer

# Complete the function below.
@qtimer.timeit
def minimumMoves(s, d):
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    d = int(input().strip())

    result = minimumMoves(s, d)

    fptr.write(str(result) + '\n')

    fptr.close()

#!/Users/anthonyquivers/anaconda3/bin/python
#Date Started: 201019

import math
import os
import random
import re
import sys
import qtimer

# Complete the function below.
@qtimer.timeit
def isValid(s):

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()

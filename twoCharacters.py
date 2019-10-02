#!/Users/anthonyquivers/anaconda3/bin/python
#Date Started: 191002

import math
import os
import random
import re
import sys

# Complete the alternate function below.
def alternate(s):

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    l = int(input().strip())

    s = input()

    result = alternate(s)

    fptr.write(str(result) + '\n')

    fptr.close()

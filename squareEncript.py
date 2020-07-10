#!/Users/anthonyquivers/anaconda3/bin/python
#Date Started: 200710

import math
import os
import random
import re
import sys
import qtimer

# Complete the function below.
@qtimer.timit
def encryption(s):

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()

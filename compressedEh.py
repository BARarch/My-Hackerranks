#!/Users/anthonyquivers/anaconda3/bin/python
#Date Started: 200326

#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'compressedString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING message as parameter.
#

def compressedString(message):
    res = ''
    prev = None
    Bundle = False
    for c in message:
        if c == prev and not Bundle:
            N = 2
            Bundle = True
        elif c == prev and Bundle:
            N += 1
        elif Bundle:
            Bundle = False
            res += prev + str(N)
        else:
            if prev is not None:
                res += prev

        prev = c
    ## End States
    if Bundle:
        res += prev + str(N)
    else:
        if prev is not None:
            res += prev
    
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    message = input()

    result = compressedString(message)

    fptr.write(result + '\n')

    fptr.close()

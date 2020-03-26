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
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    message = input()

    result = compressedString(message)

    fptr.write(result + '\n')

    fptr.close()

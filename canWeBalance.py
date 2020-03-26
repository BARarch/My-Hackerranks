#!/Users/anthonyquivers/anaconda3/bin/python
#Date Started: 200326

#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'balancedOrNot' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY expressions
#  2. INTEGER_ARRAY maxReplacements
#

def balancedOrNot(expressions, maxReplacements):
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    expressions_count = int(input().strip())

    expressions = []

    for _ in range(expressions_count):
        expressions_item = input()
        expressions.append(expressions_item)

    maxReplacements_count = int(input().strip())

    maxReplacements = []

    for _ in range(maxReplacements_count):
        maxReplacements_item = int(input().strip())
        maxReplacements.append(maxReplacements_item)

    result = balancedOrNot(expressions, maxReplacements)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()


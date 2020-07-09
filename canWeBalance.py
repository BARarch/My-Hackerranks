#!/Users/anthonyquivers/anaconda3/bin/python
#Date Started: 200326

#!/bin/python3

import math
import os
import random
import re
import sys

# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY expressions
#  2. INTEGER_ARRAY maxReplacements
#

def balancedOrNot(expressions, maxReplacements):
    
    def balancedHelp(expression, maxReplacement):
        openn = 0
        closedd = 0

        for c in expression:
            if c == "<":
                openn += 1

            if c == ">":
                closedd += 1

            if closedd > openn:
                if maxReplacement > 0:
                    maxReplacement -= 1
                    closedd -= 1
                else:
                    return 0

        if openn == closedd:
            return 1
        else:
            return 0

    res = []
    for expr, maxR in zip(expressions, maxReplacements):
        res.append(balancedHelp(expr, maxR))

    return res

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


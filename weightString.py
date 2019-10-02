#!/Users/anthonyquivers/anaconda3/bin/python
#Date Started: 191002

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the weightedUniformStrings function below.
def weightedUniformStrings(s, queries):
    from itertools import count
    import string
    weightIter = count(1)
    weights = {x: next(weightIter) for x in string.ascii_lowercase}

    substringWeights = {}
    prev = '?'
    substringSum = 0
    for c in s:
        if c == prev:
            substringSum += weights[c]        
        else:
            substringSum = weights[c]

        if substringSum not in substringWeights:
                substringWeights[substringSum] = ''
        prev = c

    res = []
    for q in queries:
        if q in substringWeights:
            res.append("Yes")
        else:
            res.append("No")
    
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input())
        queries.append(queries_item)

    result = weightedUniformStrings(s, queries)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()

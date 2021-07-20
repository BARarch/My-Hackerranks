#Date Started: 210720 

import math
import os
import random
import re
import sys
from typing import Sequence
import qtimer

# Complete the function below.
@qtimer.timeit
def calkinWilfSequence(number):
    def fractions():
        from collections import deque
        seq = deque([[1, 1]])
        while True:
            num, denom = seq.popleft()
            yield [num, denom]
            seq.append([num, denom + num])
            seq.append([num + denom, denom])


    gen = fractions()
    res = 0
    while next(gen) != number:
        res += 1
    return res

if __name__ == "__main__":
    import cs_utils
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    for var, exp in cs_utils.dict_statement_reader(sys.stdin):
        exec(var + " = " + exp)

    result = calkinWilfSequence(number) 
    fptr.write(str(result))
    fptr.write('\n')

    fptr.close()
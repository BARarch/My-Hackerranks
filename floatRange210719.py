#Date Started: 210719 

import math
import os
import random
import re
import sys
import qtimer

from itertools import count, takewhile

# Complete the function below.
@qtimer.timeit
def floatRange(start, stop, step):
    gen = takewhile(lambda x: x < stop, count(start, step))
    return list(gen)

if __name__ == "__main__":
    import cs_utils
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    for var, exp in cs_utils.dict_statement_reader(sys.stdin):
        exec(var + " = " + exp)

    
    result = floatRange(start, stop, step)
    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

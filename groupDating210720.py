#Date Started: 210720 

import math
import os
import random
import re
import sys
import qtimer

# Complete the function below.
@qtimer.timeit
def groupDating(male, female):
    return [[m  for m, f in zip(male, female) if m != f], [f  for m, f in zip(male, female) if m != f]]

if __name__ == "__main__":
    import cs_utils
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    for var, exp in cs_utils.dict_statement_reader(sys.stdin):
        exec(var + " = " + exp)

    result = groupDating(male, female) 
    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
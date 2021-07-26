#Date Started: 210721 

import math
import os
import random
import re
import sys
import qtimer

from functools import partial

def line_y(m, b, x):
    return m * x + b

# Complete the function below.
@qtimer.timeit
def twoLines(line1, line2, l, r):
    line1_y = partial(line_y, *line1)
    line2_y = partial(line_y, *line2)
    balance = 0
    for x in range(l, r + 1):
        y1 = line1_y(x)
        y2 = line2_y(x)
        if y1 > y2:
            balance += 1
        elif y1 < y2:
            balance -= 1
    if balance > 0:
        return "first"
    if balance < 0:
        return "second"
    return "any"

if __name__ == "__main__":
    import cs_utils
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    for var, exp in cs_utils.dict_statement_reader(sys.stdin):
        exec(var + " = " + exp)

    result = twoLines(line1, line2, l, r)
     
    try:
        fptr.write('\n'.join(map(str, iter(result))))
    
    except TypeError as te:
        fptr.write(str(result))
        
    fptr.write('\n')

    fptr.close()
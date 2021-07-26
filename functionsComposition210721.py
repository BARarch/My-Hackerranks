#Date Started: 210721 

import math
import os
import random
import re
import sys
import qtimer

import functools

def compose(functions):
    return lambda x: functools.reduce(lambda a, b: b(a), reversed(list(functions)), x)

# Complete the function below.
@qtimer.timeit
def functionsComposition(functions, x):
    return compose(map(eval, functions))(x)

if __name__ == "__main__":
    import cs_utils
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    for var, exp in cs_utils.dict_statement_reader(sys.stdin):
        exec(var + " = " + exp)

    result = functionsComposition(functions, x) 
    try:
        fptr.write('\n'.join(map(str, iter(result))))
    
    except TypeError as te:
        fptr.write(str(result))
        
    fptr.write('\n')

    fptr.close()
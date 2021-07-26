#Date Started: 210721 

import math
import os
import random
import re
import sys
import qtimer

def compose(f, g):
    return lambda x: f(g(x))  

# Complete the function below.
@qtimer.timeit
def simpleComposition(f, g, x):
    return compose(eval(f), eval(g))(x)

if __name__ == "__main__":
    import cs_utils
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    for var, exp in cs_utils.dict_statement_reader(sys.stdin):
        exec(var + " = " + exp)

    result = simpleComposition(f, g, x) 
    try:
        fptr.write('\n'.join(map(str, iter(result))))
    
    except TypeError as te:
        fptr.write(str(result))
        
    fptr.write('\n')

    fptr.close()
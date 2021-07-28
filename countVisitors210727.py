#Date Started: 210727 

import math
import os
import random
import re
import sys
import qtimer

# Complete the function below.
@qtimer.timeit
class Counter(object):
    def __init__(self, initValue):
        self.value = initValue

    def inc(self):
        self.value += 1

    def get(self):
        return self.value

def countVisitors(beta, k, visitors):
    counter = Counter(beta)
    for visitor in visitors:
        if visitor >= k:
            counter.inc()
    return counter.get()

if __name__ == "__main__":
    import cs_utils
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    for var, exp in cs_utils.dict_statement_reader(sys.stdin):
        exec(var + " = " + exp)

    result = countVisitors(beta, k, visitors) 
    try:
        fptr.write(' '.join(map(str, iter(result))))
    
    except TypeError as te:
        fptr.write(str(result))
        
    fptr.write('\n')

    fptr.close()
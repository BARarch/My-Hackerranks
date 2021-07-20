#Date Started: 210721 

import math
import os
import random
import re
import sys
import qtimer

class Prizes(object):
    def __init__(self, purchases, n, d):
        self.winners = map(lambda y: (y[0] + 1) * n, filter(lambda x: x[1] % d == 0, enumerate(purchases[n - 1::n])))
        
    def __iter__(self):
        return self.winners

    def __next__(self):
        pass

# Complete the function below.
@qtimer.timeit
def superPrize(purchases, n, d):
    return list(Prizes(purchases, n, d))

if __name__ == "__main__":
    import cs_utils
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    for var, exp in cs_utils.dict_statement_reader(sys.stdin):
        exec(var + " = " + exp)

    result = superPrize(purchases, n, d) 
    try:
        fptr.write('\n'.join(map(str, iter(result))))
    
    except TypeError as te:
        fptr.write(str(result))
        
    fptr.write('\n')

    fptr.close()
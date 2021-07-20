#Date Started: 210721 

import math
import os
import random
import re
import sys
import qtimer

class FRange(object):
    def __init__(self, start, stop=None, step=None):
        if stop is None:
            self.i = 0
            self.stop = start
            self.step = 1
        elif step is None:
            self.i = start
            self.stop = stop
            self.step = 1
        else:
            self.i = start
            self.stop = stop
            self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        res, self.i = self.i, self.i + self.step
        if (res < self.stop and self.step > 0) or (res > self.stop and self.step < 0):            
            return res
        else:
            raise StopIteration
            
# Complete the function below.
@qtimer.timeit
def rangeFloat(args):
    return list(FRange(*args))

if __name__ == "__main__":
    import cs_utils
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    for var, exp in cs_utils.dict_statement_reader(sys.stdin):
        exec(var + " = " + exp)

    result = rangeFloat(args) 
    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
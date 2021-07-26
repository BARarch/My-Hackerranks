#Date Started: 210721 

import math
import os
import random
import re
import sys
import qtimer

import functools

# Complete the function below.
@qtimer.timeit
def mergingVines(vines, n):
    def nTimes(n):
        def timesWrapper(func):
            def execNTimes(arg):
                for _ in range(n):
                    arg = func(arg)
                return arg
            return execNTimes
        return timesWrapper

    @nTimes(n)
    def sumOnce(vines):
        res = [vines[i] + vines[i + 1] for i in range(0, len(vines) - 1, 2)]
        if len(vines) % 2 == 1:
            res.append(vines[-1])
        return res

    return sumOnce(vines)


if __name__ == "__main__":
    import cs_utils
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    for var, exp in cs_utils.dict_statement_reader(sys.stdin):
        exec(var + " = " + exp)

    result = mergingVines(vines, n) 
    try:
        fptr.write('\n'.join(map(str, iter(result))))
    
    except TypeError as te:
        fptr.write(str(result))
        
    fptr.write('\n')

    fptr.close()
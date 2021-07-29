#Date Started: 210729 

import math
import os
import random
import re
import sys
import qtimer

import random

# Complete the function below.
@qtimer.timeit
def createDie(seed, n):
    class Die(object):
        def __init__(self, seed, n):
            self.seed = seed
            self.n = n

        def __get__(self, instance, owner):
            random.seed(self.seed)
            return str(int(random.random() * self.n) + 1)


    class Game(object):
        die = Die(seed, n)

    return Game.die


if __name__ == "__main__":
    import cs_utils
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    for var, exp in cs_utils.dict_statement_reader(sys.stdin):
        exec(var + " = " + exp)

    result = createDie(seed, n) 
    
    if isinstance(result, int) or isinstance(result, str):
        fptr.write(str(result))
    elif isinstance(result, list) or isinstance(result, tuple):
        fptr.write(str(result))
    else:
        fptr.write(' '.join(map(str, iter(result))))
        
    fptr.write('\n')

    fptr.close()
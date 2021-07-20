#Date Started: 210720 

import math
import os
import random
import re
import sys
import qtimer

class Greeter(object):
    def __init__(self, names):
        self.cnt = 0
        self.names = names

    def __iter__(self):
        return self

    def __next__(self):
        if self.cnt < len(self.names):
            self.cnt += 1
            return 'Hello, {}!'.format(self.names[self.cnt - 1])
        else:
            raise StopIteration

# Complete the function below.
@qtimer.timeit
def greetingsGenerator(team):
    return list(Greeter(team))

if __name__ == "__main__":
    import cs_utils
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    for var, exp in cs_utils.dict_statement_reader(sys.stdin):
        exec(var + " = " + exp)

    result = greetingsGenerator(team) 
    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
#Date Started: 210727 

import math
import os
import random
import re
import sys
import qtimer

class Rectangle(object):
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def __str__(self):
        return '{} x {} = {}'.format(self.height, self.width, self.area)

    @property
    def area(self):
        return self.height * self.width

# Complete the function below.
@qtimer.timeit
def primarySchool(height, width):
    return str(Rectangle(height, width))

if __name__ == "__main__":
    import cs_utils
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    for var, exp in cs_utils.dict_statement_reader(sys.stdin):
        exec(var + " = " + exp)

    result = primarySchool(height, width) 
    try:
        fptr.write(' '.join(map(str, iter(result))))
    
    except TypeError as te:
        fptr.write(str(result))
        
    fptr.write('\n')

    fptr.close()
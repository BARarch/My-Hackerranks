#Date Started: 210727 

import math
import os
import random
import re
import sys
import qtimer

class User(object):
    def __init__(self, username, _id, xp, name):
        self.username = username
        self._id = _id
        self.xp = xp
        self.name = name
    
    def __getattr__(self, name):
        return f'{name} attribute is not defined'


# Complete the function below.
@qtimer.timeit
def userAttribute(attribute):
    user = User("annymaster", "1234567", "1500", "anny")
    return getattr(user, attribute)

if __name__ == "__main__":
    import cs_utils
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    for var, exp in cs_utils.dict_statement_reader(sys.stdin):
        exec(var + " = " + exp)

    result = userAttribute(attribute)

    if isinstance(result, int) or isinstance(result, str):
        fptr.write(str(result))
    elif isinstance(result, list) or isinstance(result, tuple):
        fptr.write(str(result))
    else:
        fptr.write(' '.join(map(str, iter(result))))
        
    fptr.write('\n')

    fptr.close()
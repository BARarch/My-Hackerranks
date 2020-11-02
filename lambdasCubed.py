#!/Users/anthonyquivers/anaconda3/bin/python
#Date Started: 201102

import math
import os
import random
import re
import sys
import qtimer

# Complete the function below.
@qtimer.timeit
cube = lambda x: x ** 3 # complete the lambda function 

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
    # return a list of fibonacci numbers

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))

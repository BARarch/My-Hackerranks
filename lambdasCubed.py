#!/Users/anthonyquivers/anaconda3/bin/python
#Date Started: 201102

import math
import os
import random
import re
import sys
import qtimer

cube = lambda x: x**3  # complete the lambda function


# Complete the function below.
@qtimer.timeit
def fibonacci(n):
    if n <= 1:
        return list(range(n))

    res = list(range(2))
    for i in range(n - 2):
        res.append(res[-2] + res[-1])
    return res
    # return a list of fibonacci numbers


if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))

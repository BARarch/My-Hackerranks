#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#

def minimumBribes(q):
    from itertools import count
    
    window = [1, 2, 3]
    upperBound = count(4)
    nBribes = 0

    for num in q:  
        if num in window:
            nBribes += window.index(num)
            window.remove(num)
            window.append(next(upperBound))    
        else:
            print("Too chaotic")
            return
        
    print(nBribes)
    return
    

        
        
    

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)

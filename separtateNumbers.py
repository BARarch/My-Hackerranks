#!/Users/anthonyquivers/anaconda3/bin/python
#Date Started: 190928


import math
import os
import random
import re
import sys

# Complete the separateNumbers function below.
def separateNumbers(s):
    from itertools import count
    if len(s) < 2:
        return "NO"
    
    end = 1
    while end <= len(s) / 2:
        initt = s[:end]
        seq = count(int(initt))
        beautifulNum = ''
        while len(beautifulNum) < len(s):
            beautifulNum += str(next(seq))
        
        if beautifulNum == s:
            return "YES {}".format(str(initt))
        else:
            end += 1
    
    return "NO"

    

if __name__ == '__main__':
    q = int(input())

    for q_itr in range(q):
        s = input()

        print(separateNumbers(s))

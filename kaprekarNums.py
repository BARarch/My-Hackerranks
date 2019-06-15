#!/Users/anthonyquivers/anaconda3/bin/python
#Date Started: 190608

import math
import os
import random
import re
import sys

# Complete the kaprekarNumbers function below.
def kaprekarNumbers(p, q):
    keps = []
    for n in range(p, q + 1):
        if n ** 2 < 10:
            s = '0' + str(n ** 2)
        else:
            s = str(n ** 2)
        #print(s)
        #print(len(s))
        l = int(s[:(len(s) // 2)])
        r = int(s[(len(s) // 2):])

        #print('left:' + str(l))
        #print('right:' + str(r))

        if ((l + r) == n):
            keps.append(n)

    if keps:
        print(' '.join(map(str, keps)))
    else:
        print('INVALID RANGE')

        

if __name__ == '__main__':
    p = int(input())

    q = int(input())

    kaprekarNumbers(p, q)

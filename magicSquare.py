#!/Users/anthonyquivers/anaconda3/bin/python
#Date Started: 191013

#!/bin/python3

import sys

def formingMagicSquare(s):
    # Complete this function

if __name__ == "__main__":
    s = []
    for s_i in range(3):
       s_t = [int(s_temp) for s_temp in input().strip().split(' ')]
       s.append(s_t)
    result = formingMagicSquare(s)
    print(result)

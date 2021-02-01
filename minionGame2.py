#!/Users/anthonyquivers/anaconda3/bin/python
#Date Started: 200924

import math
import os
import random
import re
import sys
import qtimer


# Complete the function below.
@qtimer.timeit
def minion_game(string):
    l = len(string)
    n = 0
    vowels = "AEIOU"
    kevinScore = 0
    stuartScore = 0

    cWords = {}
    vWords = {}

    for c in string:
        if c in vowels:
            kevinScore += l - n
        else:
            stuartScore += l - n
        n += 1

    if kevinScore == stuartScore:
        print("Draw")
    elif kevinScore > stuartScore:
        print('Kevin {}'.format(str(kevinScore)))
    else:
        print('Stuart {}'.format(str(stuartScore)))


if __name__ == '__main__':
    s = input()
    minion_game(s)

#!/Users/anthonyquivers/anaconda3/bin/python
#Date Started: 190618


import math
import os
import random
import re
import sys

# Complete the happyLadybugs function below.


def happyLadybugs(b):
    print(b)

    ## Sort and Make sure there is no lonely ladybug
    if "_" in b:
        state = "YES"
        prev = 'a'
        for color in sorted(b):
            if color == '_':
                return state
            if color != prev:
                ## Ladybug must be happy by the time we switch colors
                if state == "NO":
                    return state
                else:
                    state = "NO"
            else:
                state = "YES"
            prev = color

    ## No "_" No Sort
    else:
        state = "YES"
        prev = 'a'
        for color in b:
            if color != prev:
                ## Ladybug must be happy by the time we switch colors
                if state == "NO":
                    return state
                else:
                    state = "NO"
            else:
                state = "YES"
            prev = color

        return state
    return 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input())

    for g_itr in range(g):
        n = int(input())

        b = input()

        result = happyLadybugs(b)

        fptr.write(result + '\n')

    fptr.close()

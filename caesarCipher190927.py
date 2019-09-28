#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the caesarCipher function below.
def caesarCipher(s, k):
    def letter_to_map(k):
        def fun(c):
            if not c.isalpha():
                return c
            if c.isupper():
                letters = 'abcdefghijklmnopqrstuvwxyz'.upper()
                return letters[((letters.index(c) + k) % 26)]
            else:   
                letters = 'abcdefghijklmnopqrstuvwxyz'
                return letters[((letters.index(c) + k) % 26)]
        return fun
    shift = letter_to_map(k)
    return ''.join(map(shift, s))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    k = int(input())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()


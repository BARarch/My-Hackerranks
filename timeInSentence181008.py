#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the timeInWords function below.
def timeWords(time):
    tWs = {   1: 'one',
                2: 'two',
                3: 'three',
                4: 'four',
                5: 'five',
                6: 'six',
                7: 'seven',
                8: 'eight',
                9: 'nine',
                10: 'ten',
                11: 'eleven',
                12: 'twelve',
                13: 'thirteen',
                14: 'fourteen',
                15: 'quarter',
                16: 'sixteen',
                17: 'seventeen',
                18: 'eighteen',
                19: 'nineteen',
                20: 'twenty',
                30: 'half'}
    return tWs[time]

def mintutesInWords(m):
    if m == 1:
        return 'one minute'
    if m == 15:
        return 'quarter'
    if m == 30:
        return 'half'
    if m > 20:
        return 'twenty {} minutes'.format(timeWords(m - 20))
    else:
        return '{} minutes'.format(timeWords(m))

def timeInWords(h, m):
    if m == 0:
        return "{} o' clock".format(timeWords(h))
    elif m <= 30:
        return '{} past {}'.format(mintutesInWords(m), timeWords(h))
    else:
        return '{} to {}'.format(mintutesInWords(60 - m), timeWords((h + 1) % 12))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = int(input())

    m = int(input())

    result = timeInWords(h, m)

    fptr.write(result + '\n')

    fptr.close()

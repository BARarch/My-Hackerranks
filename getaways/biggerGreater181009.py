#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the biggerIsGreater function below.
def swap(w, a, b):
    ## Swap Charaters and indexes a and b
    ## b is greater than a
    return w[:a] + w[b] + w[a+1:b] + w[a] + w[b+1:]

def test_swap(w, a, b=None):
    ## Create a test Sting to comapare with swap characters at a and b
    ## b is greater than a if not None
    if b is None:
        return ('a' * a) + w[a] + ('a' * (len(w) - a - 1))
    else:
        return ('a' * a) + w[b] + ('a' * (b - a - 1)) + w[a] + ('a' * (len(w) - b - 1))
    
def compose_test_swap(w, a, b=None):
    if b is None:
        return [(a, ''), test_swap(w, a)]
    else:
        return [(a, b), test_swap(w, a, b)]

def compose(a, b, testResult):
    return [(a, b), testResult]
    
def swap_b(swap):
    return swap[0][0]

def swap_b(swap):
    return swap[0][1]

def swap_result(swap):
    return swap[1]

def biggerIsGreater(w):
    return test_swap(w, 0, 1)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input())

    for T_itr in range(T):
        w = input()

        result = biggerIsGreater(w)

        fptr.write(result + '\n')

    fptr.close()

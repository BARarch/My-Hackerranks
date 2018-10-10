'''#!/bin/python3'''

import math
import os
import random
import re
import sys

# Complete the biggerIsGreater function below.
def execute_swap(w, a, b):
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
    
def test_compose_swap(w, a, b=None):
    if b is None:
        return ((a, ''), test_swap(w, a))
    else:
        return ((a, b), test_swap(w, a, b))

def compose_swap(a, b, testResult):
    return ((a, b), testResult)
    
def swap_a(swap):
    return swap[0][0]

def swap_b(swap):
    return swap[0][1]

def swap_result(swap):
    return swap[1]

## This is the fitler run in a loop for the lows of an iteration
## for each confirmed swap at this level
def low_unswaped(swaped_b):
    return lambda swaped_low: swap_b(swaped_low) != swaped_b

def has_been_swaped(start, swaps):
    for swap in swaps:
        if swap_b(swap) == start:
            return True
    return False

def compute_swaps(w, start):
    ## This is the recusive function that works for the charater
    ## at index 'start' for string 'w' and all charaters to the right of it
    ## this function may return:
    ## a list with a single swap
    ## a list of swaps
    ## or an empty list

def biggerIsGreater(w):
    swaps = compute_swaps(w, len(w - 2))
    if swaps:
        for swap in swaps:
            w = execute_swap(w, swap_a(swap), swap_b(swap))
        return w
    else:
        return 'no anwser'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input())

    for T_itr in range(T):
        w = input()

        result = biggerIsGreater(w)

        fptr.write(result + '\n')

    fptr.close()

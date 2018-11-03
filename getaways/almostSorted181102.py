#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the almostSorted function below.
def almostSorted(arr):
	peaks = []
	vals = []
	last = None
	n = 1
	increasing = True
	for c in arr:
	    #s = sorted(arr)
	    if increasing:
	    	if c < last:
	    		peaks.append(n - 1)
	    		increasing = False
	    else:
	    	if c > last:
	    		vals.append(n - 1)
	    		increasing = True
    	last = c
    	n += 1

    return 'no'

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    almostSorted(arr)

#!/bin/python3

import math
import os
import random
import re
import sys

def full_mask(r, c):
    pass

def right_mask(r, c):
    pass

def left_mask(r, c):
    pass

def make_calc_north(r, c):
    pass

def make_calc_east(r, c):
    pass

def make_calc_south(r, c):
    pass

def make_calc_west(r, c):
    pass

def count_ones(val):
    pass

def calc_tops(val, next):
    pass

# Complete the surfaceArea function below.
def surfaceArea(A):
    curr = 'Read Base to int'
    level = 1
    nextt = 'Read Next level of stack to int'
    
    sumArea = 'Bottom Calc'
    sumArea += 'North Calc'
    sumArea += 'East Calc'
    sumArea += 'South Calc'
    sumArea += 'West Calc'
    sumArea += 'Top Calc'
    
    while nextt:
        curr = nextt
        level += 1
        nextt = 'Read Next Level'
        
        sumArea += 'North Calc'
        sumArea += 'East Calc'
        sumArea += 'South Calc'
        sumArea += 'West Calc'
        sumArea += 'Top Calc'
        
    return sumArea

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    HW = input().split()

    H = int(HW[0])

    W = int(HW[1])

    A = []

    for _ in range(H):
        A.append(list(map(int, input().rstrip().split())))

    result = surfaceArea(A)

    fptr.write(str(result) + '\n')

    fptr.close()

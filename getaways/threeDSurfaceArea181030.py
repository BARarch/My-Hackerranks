#!/bin/python3

import math
import os
import random
import re
import sys

class TestCase:
    def __init__(self, file):
        f = open(file, 'r')
        HW = list(map(int, f.readline().rstrip().split(' ')))

        self.h = HW[0]
        self.w = HW[1]
        self.A = []

        for _ in range(self.h):
            self.A.append(list(map(int, f.readline().rstrip().split(' '))))

        f.close()

    def get_h(self):
        return self.h

    def get_w(self):
        return self.w

    def get_A(self):
        return self.A


def full_mask(r, c):
    return (2 ** (r * c)) - 1

def right_mask(r, c):
    ## Have c columns, need a number with c - 1 ones
    base = ((2 ** (c - 1)) - 1)
    mask = 0
    for _ in range(r):
        mask <<= c
        mask |= base
    return mask
    

def left_mask(r, c):
    ## Have c columns, need a number with c - 1 ones then one 0
    base = ((2 ** (c - 1)) - 1) << 1
    mask = 0
    for _ in range(r):
        mask <<= c
        mask |= base
    return mask

def make_calc_north(r, c):
    pass

def make_calc_east(r, c):
    pass

def make_calc_south(r, c):
    pass

def make_calc_west(r, c):
    pass

def count_ones(val):
    return bin(val)[2:].count('1')

def calc_tops(val, nextt):
    return count_ones(val ^ nextt)

def make_section_next(A):
    ## Generator that gives sections for successive levels
    ## of A with each call.
    pass

# Complete the surfaceArea function below.
def surfaceArea(A):
    curr = 'Read Base to int'
    level = 1
    nextt = 'Read Next level of stack to int'
    
    sumArea = count_ones(curr)      # Bottom
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

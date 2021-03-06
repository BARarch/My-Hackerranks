import math
import os
import random
import re
import sys

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
    ## The north side calcs shift the cells from the north
    ## DOWN to the space, calculate
    #fullMask = full_mask(r, c)
    def north_calc(val):
        return val & (val ^ val >> c)
    return north_calc 
    
def make_calc_east(r, c):
    ## The east side calcs shift the cells from the east
    ## RIGHT to the space, calculate
    ## We will need a right mask
    rightMask = right_mask(r, c)
    def east_calc(val):
        return val & (val ^ (rightMask & (val >> 1)))
    return east_calc


def make_calc_south(r, c):
    ## The south side calcs shift the cells from the south
    ## UP to the space, calculate
    fullMask = full_mask(r, c)
    def south_calc(val):
        return val & (val ^ (fullMask & (val << c)))
    return south_calc 

def make_calc_west(r, c):
    ## The west side calcs shift the cells from the west
    ## LEFT to the space, calculate
    ## We will need a left mask
    leftMask = left_mask(r, c)
    def west_calc(val):
        return val & (val ^ (leftMask & (val << 1)))
    return west_calc

def count_ones(val):
    return bin(val)[2:].count('1')

def calc_tops(val, nextt):
    return val ^ nextt

def make_section_next(A):
    ## Generator that gives sections for successive levels
    ## of A with each call.
    n = 0
    while True:
        val = 0
        for row in A:
            for c in row:
                val <<= 1
                if c > n:
                    val |= 1
        yield val
        n += 1

def decode_section(val, r, c):
    sect = []
    col = 0
    row = ''
    binVal = bin(val)[2:]
    binVal = ('0' * ((r * c) - len(binVal))) + binVal

    for start in range(0, len(binVal), c):
        sect.append(binVal[start:start + c])
    return sect

def print_decode_section(val, r, c):
    sectionList = decode_section(val, r, c)
    for row in sectionList:
        print(row)

# Complete the surfaceArea function below.
def surfaceArea(A):
    h = len(A)
    w = len(A[0])

    north_calc = make_calc_north(h, w)
    east_calc = make_calc_east(h, w)
    south_calc = make_calc_south(h, w)
    west_calc = make_calc_west(h, w)

    section = make_section_next(A)

    curr = next(section)
    nextt = next(section)
    
    sumArea = count_ones(curr)      # Bottom
    sumArea += count_ones(north_calc(curr))
    sumArea += count_ones(east_calc(curr))
    sumArea += count_ones(south_calc(curr))
    sumArea += count_ones(west_calc(curr))
    sumArea += count_ones(calc_tops(curr, nextt))
    
    while nextt:
        curr = nextt
        nextt = next(section)
        
        sumArea += count_ones(north_calc(curr))
        sumArea += count_ones(east_calc(curr))
        sumArea += count_ones(south_calc(curr))
        sumArea += count_ones(west_calc(curr))
        sumArea += count_ones(calc_tops(curr, nextt))
        
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

#!/Users/anthonyquivers/anaconda3/bin/python
#Date Started: 201030

import math
import os
import random
import re
import sys
import qtimer


# Complete the function below.
@qtimer.timeit
def connectedCell(matrix):
    def neighbors(x, y):
        ## Top Row
        if x > 0 and y > 0:
            yield x - 1, y - 1
        if y > 0:
            yield x, y - 1
        if x + 1 < len(matrix[0]) and y > 0:
            yield x + 1, y - 1
        ## Middle
        if x > 0:
            yield x - 1, y
        if x + 1 < len(matrix[0]):
            yield x + 1, y
        ## Bottom Row
        if x > 0 and y + 1 < len(matrix):
            yield x - 1, y + 1
        if y + 1 < len(matrix):
            yield x, y + 1
        if x + 1 < len(matrix[0]) and y + 1 < len(matrix):
            yield x + 1, y + 1

    ones = set()
    for i, row in enumerate(matrix):
        for j, val in enumerate(row):
            if val:
                ones.add((j, i))

    largest = 0
    while ones:
        currentRegion = [ones.pop()]
        currentSize = 1
        while currentRegion:
            cell = currentRegion.pop(0)
            for neighbor in neighbors(*cell):
                if neighbor in ones:
                    currentRegion.append(neighbor)
                    currentSize += 1
                    ones.remove(neighbor)

        if currentSize > largest:
            largest = currentSize

    return largest


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    m = int(input())

    matrix = []

    for _ in range(n):
        matrix.append(list(map(int, input().rstrip().split())))

    result = connectedCell(matrix)

    fptr.write(str(result) + '\n')

    fptr.close()

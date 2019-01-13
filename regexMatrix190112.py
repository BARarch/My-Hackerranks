import math
import os
import random
import re
import sys

def strIter(item, m):
    item = item + (' ' * (m - len(item)))
    for char in item:
        yield char

def replc(string, m):
    return string[:m.start()] + " " + string[m.end():]

flanks = re.compile(r'(?<=[^\W_])([\W_]+)(?=[^\W_])')    


nm = input().split()

n = int(nm[0])

m = int(nm[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(strIter(matrix_item, m))

#print(len(matrix))
baseStr = ''
for _ in range(m):
    for itera in matrix:
        baseStr += next(itera)

#print("before")
#print(baseStr)
for m in reversed(list(flanks.finditer(baseStr))):
    #print(m)
    baseStr = replc(baseStr, m)

#print('after')
print(baseStr)

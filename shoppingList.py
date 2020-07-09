#!/Users/anthonyquivers/anaconda3/bin/python
#Date Started: 200115

#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'getNumberOfOptions' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY priceOfJeans
#  2. INTEGER_ARRAY priceOfShoes
#  3. INTEGER_ARRAY priceOfSkirts
#  4. INTEGER_ARRAY priceOfTops
#  5. INTEGER budgeted
#

def getNumberOfOptions(priceOfJeans, priceOfShoes, priceOfSkirts, priceOfTops, budgeted):
    # Write your code here
    pJeans = sorted(priceOfJeans)
    pShoes = sorted(priceOfShoes)
    pSkirts = sorted(priceOfSkirts)
    pTops = sorted(priceOfTops)
    J = {}
    SH = {}
    SK = {}
    T = {}

    def jeans(b):
        if b < 0:
            return 0
        if b in J:
            return J[b]

        nItems = 0
        for cost in pJeans:
            if b - cost < 0:
                J[b] = nItems
                return nItems
            nItems += shoes(b - cost)
        J[b] = nItems
        return nItems
        
    def shoes(b):
        if b < 0:
            return 0
        if b in SH:
            return SH[b]

        nItems = 0
        for cost in pShoes:
            if b - cost < 0:
                SH[b] = nItems
                return nItems
            nItems += skirts(b - cost)
        SH[b] = nItems
        return nItems

    def skirts(b):
        if b < 0:
            return 0
        if b in SK:
            return SK[b]

        nItems = 0
        for cost in pSkirts:
            if b - cost < 0:
                SK[b] = nItems
                return nItems
            nItems += tops(b - cost)
        SK[b] = nItems
        return nItems
                
    def tops(b):
        if b < 0:
            return 0
        if b in T:
            return T[b]
        else:
            if pTops[-1] <= b:
                T[b] = len(pTops)
                return len(pTops)
            nItems = 0
            for cost in pTops:
                if cost <= b:
                    nItems += 1
                else:
                    T[b] = nItems
                    return nItems

    return jeans(budgeted)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    priceOfJeans_count = int(input().strip())

    priceOfJeans = []

    for _ in range(priceOfJeans_count):
        priceOfJeans_item = int(input().strip())
        priceOfJeans.append(priceOfJeans_item)

    priceOfShoes_count = int(input().strip())

    priceOfShoes = []

    for _ in range(priceOfShoes_count):
        priceOfShoes_item = int(input().strip())
        priceOfShoes.append(priceOfShoes_item)

    priceOfSkirts_count = int(input().strip())

    priceOfSkirts = []

    for _ in range(priceOfSkirts_count):
        priceOfSkirts_item = int(input().strip())
        priceOfSkirts.append(priceOfSkirts_item)

    priceOfTops_count = int(input().strip())

    priceOfTops = []

    for _ in range(priceOfTops_count):
        priceOfTops_item = int(input().strip())
        priceOfTops.append(priceOfTops_item)

    budgeted = int(input().strip())

    result = getNumberOfOptions(priceOfJeans, priceOfShoes, priceOfSkirts, priceOfTops, budgeted)

    fptr.write(str(result) + '\n')

    fptr.close()


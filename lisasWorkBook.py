#!/Users/anthonyquivers/anaconda3/bin/python
#Date Started: 190608

import math
import os
import random
import re
import sys

# Complete the workbook function below.
def workbook(n, k, arr):
    startPage = 1
    nSpecialNumbers = 0

    #print('k = ' + str(k))
    #print()

    for nProbs in arr:      ## For every chapter
        reqPages = math.ceil(nProbs / k)
        firstProbOnPage = 1
        #print()
        #print("chapter with " + str(nProbs) + " problems")
        for page in range(startPage, startPage + reqPages):  ## For every page in chapter
            #print("Page Number " + str(page) + str(list(range(firstProbOnPage, firstProbOnPage + k))), end=' ')
    
            if page in list(range(firstProbOnPage, firstProbOnPage + k)):
                ## This is a special Number
                if page <= nProbs:
                    nSpecialNumbers += 1
                    #print("Special Number")


            firstProbOnPage += k

        startPage += reqPages

    return nSpecialNumbers  

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = workbook(n, k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()


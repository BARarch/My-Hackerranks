#Date Started: 211113 

import math
import os
import random
import re
import sys
import qtimer

# Complete the function below.
@qtimer.timeit
def swapMaxSumMatrix(matrix):
    n = len(matrix) // 2
    def transpose(matrix):
        trans = [[0, ] * len(matrix)] * len(matrix)
        
        '''print("Mat")
        for row in matrix:
            print(row)

        print ("trans")'''
        for i in range(len(matrix)):
            trans[i] = [matrix[j][i] for j in range(len(matrix))]

            '''for row in trans:
                print(row)'''
        return trans
    
    swaps = 1
    
    while swaps > 0:
        swaps = 0
        ## Algoriz
        # Compare Rows in quadrants 1 and 2
        for row in matrix[:n]: ##Top Half
            if sum(row[n:]) > sum(row[:n]):
                row.reverse()
                swaps += 1

        # Compare Rows in quadrants 3 and 4
        for row in matrix[n:]: ## Bottom Half
            if sum(row[:n]) > sum(row[n:]):
                row.reverse()
                swaps += 1
                
        # Transposed to Compare Colunms in quadrants 2 and 4 now
        matrix = transpose(matrix)
        for row in matrix[n:]: ## Bottom Half
            if sum(row[n:]) > sum(row[:n]):
                row.reverse()
                swaps += 1
                
        # Transpose it back to Compare the rows of quadrants 1 and 2
        matrix = transpose(matrix)
        for row in matrix[:n]: ## Top Half
            if sum(row[n:]) > sum(row[:n]):
                row.reverse()
                swaps += 1

        print(f'nSwaps: {swaps}')
        for row in matrix:
            print(row)
         
                
    res = 0
    for row in matrix[:n]:
        res += sum(row[:n])
    
    return res

def laserQuadSum(matrix):
    n = len(matrix) // 2
    k = len(matrix) - 1
    summ = 0

    for i, row in enumerate(matrix[:n]):
        for j, q in enumerate(row[:n]):
            summ += max(q, matrix[i][k - j], matrix[k - i][k - j], matrix[k - i][j])

    return summ


if __name__ == "__main__":
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())
    s = int(input()) * 2

    mat = []
    for _ in range(s):
        mat.append(list(map(int, input().rstrip().split(" "))))

    ans = laserQuadSum(mat)

    fptr.write(str(ans) + '\n')

    fptr.close()
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the queensAttack function below.
def queensAttack(n, k, r_q, c_q, obstacles):
    #n: width and height of board
    #k: number of obstacles

    def make_board(S, obstacles):
        def get_row(obstacle):
            return obstacle[0]

        def get_col(obstacle):
            return obstacle[1]

        for obj in obstacles:
            S[get_row(obj) - 1] |= 1 << (n - get_col(obj))

    def show_board(S):
        width = len(S)
        for row in reversed(S):
            ## Fixed Width Binary number
            print(('{0:0' + str(width) + 'b}').format(row))

    S = [0] * n                 #an number on the list for each row
    make_board(S, obstacles)

    #show_board(S)
    return 0


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    r_qC_q = input().split()

    r_q = int(r_qC_q[0])

    c_q = int(r_qC_q[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)

    fptr.write(str(result) + '\n')

    fptr.close()

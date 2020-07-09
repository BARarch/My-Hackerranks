#!/Users/anthonyquivers/anaconda3/bin/python
#Date Started: 190608

import math
import os
import random
import re
import sys

# Complete the queensAttack function below.
def queensAttack(n, k, r_q, c_q, obstacles):
    #n: width and height of board
    #k: number of obstacles

    def init_moves(row, column):
        from itertools import repeat
        # Functions that return interators for each moves
        # Evaluate them to count spaces
        # Remember
        # (row, colunm)
        # positive row: UP
        # positive column: Right
        # positions are numbered from 1 to n
        N = zip(range(row + 1, n + 1), repeat(column))
        NE = zip(range(row + 1, n + 1), range(column + 1, n + 1))
        E = zip(repeat(row), range(column + 1, n + 1))
        SE = zip(reversed(range(1, row)), range(column + 1, n + 1))
        S = zip(reversed(range(1, row)), repeat(column))
        SW = zip(reversed(range(1, row)), reversed(range(1, column)))
        W = zip(repeat(row), reversed(range(1, column)))
        NW = zip(range(row + 1, n + 1), reversed(range(1, column)))

        return [N, NE, E, SE, S, SW, W, NW]

    # Throw Obsticles in a Hash
    obstacles = {tuple(piece) : 0 for piece in obstacles}
    #print(obstacles)

    directions = init_moves(r_q, c_q)
    nMoves = 0
    for direction in directions:
        for move in direction:
            if move in obstacles:
                # Drop Direction
                break
            nMoves += 1
        

    return nMoves


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

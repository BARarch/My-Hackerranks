#!/Users/anthonyquivers/anaconda3/bin/python
#Date Started: 190718


import math
import os
import random
import re
import sys

# Complete the minimumMoves function below.
def minimumMoves(grid, startX, startY, goalX, goalY):
    from itertools import repeat
    from queue import SimpleQueue, Queue

    def init_move_functs(grid):
        n = len(grid)
        def left(x, y):  #left move negative y to 0
            return zip(repeat(x), reversed(range(y)))
        def right(x, y): # right move positive y to n
            return zip(repeat(x), range(y + 1, n))
        def up(x, y): # up move negative x to 0
            return zip(reversed(range(0, x)), repeat(y))
        def down(x, y): # down move positive x to n
            return zip(reversed(range(x + 1, n)), repeat(y))
        return [left, up, right, down]

    def pickle_grid(grid):
        def pickle(x, y):
            return grid[x][y]
        return pickle

    moves = init_move_functs(grid)
    obstacles = pickle_grid(grid)
    nMoves = Queue()
    childrenMoves = Queue()   
    ## How to evaluate moves from a point
    #point = (0, 0)
    #print(list(moves[3](*point)))

    start = (startX, startY)
    goal = (goalX, goalY)
    visited = {}

    #Place in all children 1 move from start
    for move in moves:
        childrenMoves.put(move(*(start)))
        nMoves.put(1)

    # Begin BFS
    while True:
        arm = childrenMoves.get_nowait()
        n = nMoves.get_nowait()
        for point in arm:
            #print(point)
            # Visited Case
            if point in visited:
                # Skip dont check or add children
                continue
            # Base Case
            if point == goal:
                return n   
            # Obstacle Case
            if obstacles(*(point)) == "X":
                break   # Drop move hit obstacle
            # Add Children Case
            visited[point] = n
            
            for move in moves:
                childrenMoves.put(move(*(point)))
                nMoves.put(n + 1)  
        print(nMoves.qsize()) 

    return "Too Bigs"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    startXStartY = input().split()

    startX = int(startXStartY[0])

    startY = int(startXStartY[1])

    goalX = int(startXStartY[2])

    goalY = int(startXStartY[3])

    result = minimumMoves(grid, startX, startY, goalX, goalY)

    fptr.write(str(result) + '\n')

    fptr.close()


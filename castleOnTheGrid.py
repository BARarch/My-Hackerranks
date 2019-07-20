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
    from queue import Queue

    def init_move_functs(grid):
        n = len(grid)
        def left(x, y, step, prev, direction):  #left move negative y to 0
            return zip(repeat(x), reversed(range(y)), repeat(step + 1), repeat((x, y)), repeat("LEFT"))
        def right(x, y, step, prev, direction): # right move positive y to n
            return zip(repeat(x), range(y + 1, n), repeat(step + 1), repeat((x, y)), repeat("RIGHT"))
        def up(x, y, step, prev, direction): # up move negative x to 0
            return zip(reversed(range(0, x)), repeat(y), repeat(step + 1), repeat((x, y)), repeat("UP"))
        def down(x, y, step, prev, direction): # down move positive x to n
            return zip(range(x + 1, n), repeat(y), repeat(step + 1), repeat((x, y)), repeat("DOWN"))
        return [left, up, right, down]

    def pickle_grid(grid):
        def pickle(x, y):
            return grid[x][y]
        return pickle

    moves = init_move_functs(grid)
    obstacles = pickle_grid(grid)
    childrenMoves = Queue()   

    start = (startX, startY, 0, None, None)
    goal = (goalX, goalY)
    visited = {start[:2]: 0}

    #Place in all children 1 move from start
    for move in moves:
        childrenMoves.put(move(*(start)))

    # Begin BFS
    while True:
        direction = childrenMoves.get_nowait()
        for point in direction:
            # Base Case
            if point[:2] == goal:
                return point[2]   
            # Obstacle Case
            if obstacles(*(point[:2])) == "X":
                break   # Drop move hit obstacle
            # Visited Case
            if point[:2] in visited:
                # Skip dont check or add children
                continue
            # Add Children Case
            visited[point[:2]] = point[2]          
            for move in moves:
                childrenMoves.put(move(*(point))) 

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


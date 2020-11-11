import math
import os
import random
import re
import sys


def hanoi(start, buff, end, n):
    if n == 1:
        end.append(start.pop())
        #print(f'n = {n}')
        print(f'stack1: {H["stack1"]}')
        print(f'stack2: {H["stack2"]}')
        print(f'stack3: {H["stack3"]}')
        print()
    else:
        hanoi(start, end, buff, n - 1)
        end.append(start.pop())
        hanoi(buff, start, end, n - 1)


if __name__ == "__main__":

    H = {"stack1": [6, 5, 4, 3, 2, 1], "stack2": [], "stack3": []}

    #stack1 = [6, 5, 4, 3, 2, 1]
    #stack2 = []
    #stack3 = []

    hanoi(H['stack1'], H['stack2'], H["stack3"], 6)
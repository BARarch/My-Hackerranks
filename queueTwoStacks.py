#!/Users/anthonyquivers/anaconda3/bin/python
#Date Started: 201014

import math
import os
import random
import re
import sys
import qtimer

# Complete the function below.

push = []
pop = []


def refresh(a, b):
    while a:
        b.append(a.pop())


def enqueue(num):
    push.append(num)


def front():
    if pop:
        return pop[-1]
    else:
        refresh(push, pop)
        return pop[-1]


def dequeue():
    if pop:
        pop.pop()
    else:
        refresh(push, pop)
        pop.pop()


@qtimer.timeit
def aS(N):
    for _ in range(N):
        x = map(int, input().split(' '))
        cmd = next(x)
        if cmd == 1:
            enqueue(next(x))
        if cmd == 2:
            dequeue()
        if cmd == 3:
            print(front())


s1 = []
s2 = []


def q_append(x):
    if s2:
        while s2:
            s1.append(s2.pop())
    s1.append(x)


def q_pop():
    if s1:
        while s1:
            s2.append(s1.pop())
    s2.pop()


def peek():
    if s1:
        while s1:
            s2.append(s1.pop())
    return s2[-1]


@qtimer.timeit
def pS(q):
    for i in range(q):
        line = re.split(' ', sys.stdin.readline())
        type = int(line[0])
        if type == 1:
            x = line[1]
            q_append(x)
        if type == 2:
            q_pop()
        if type == 3:
            print(peek(), end="")


if __name__ == "__main__":
    N = int(input())
    aS(N)
    #pS(N)

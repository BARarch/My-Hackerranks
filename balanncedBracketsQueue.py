#!/Users/anthonyquivers/anaconda3/bin/python
#Date Started: 200930

import math
import os
import random
import re
import sys
import qtimer


# Complete the function below.
@qtimer.timeit
def isBalanced(s):
    closed = ")}]"
    opening = "({["
    bracketMatch = {')': '(', '}': '{', ']': '['}

    brackets = deque([])

    for c in s:
        if c in closed:
            if len(brackets) == 0 or brackets.pop() != bracketMatch[c]:
                print(f"end early for {s}")
                print(f'character {c}')
                print(f'brackets {brackets}')
                return "NO"
        elif c in opening:
            brackets.append(c)

    return "YES" if len(brackets) == 0 else "NO"


if __name__ == '__main__':
    from collections import deque
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()

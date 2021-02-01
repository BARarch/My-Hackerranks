#!/Users/anthonyquivers/anaconda3/bin/python
#Date Started: 200710

import math
import os
import random
import re
import sys
import qtimer


# Complete the function below.
@qtimer.timeit
def encryption(s):
    def square_encryption(s, r, c):
        def matrixIterator(s, r, c):
            def rowIter(chunk):
                print(chunk)
                for s in chunk:
                    yield s

            for U in zip(*[rowIter(s[x * c:(x + 1) * c]) for x in range(r)]):
                yield U

        ## Add Spaces to fill rows
        nAddedSpaces = c - (len(s) % c)
        s += " " * nAddedSpaces

        ## Additional Row if their are not enough components
        if r * c < len(s):
            r += 1

        for i in matrixIterator(s, r, c):
            yield ''.join(i).strip(' ')

    sr = math.sqrt(len(s))
    r = math.floor(sr)
    c = math.ceil(sr)
    return " ".join(square_encryption(s, r, c))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()

#!/Users/anthonyquivers/anaconda3/bin/python
#Date Started: 200806

import math
import os
import random
import re
import sys
import qtimer


# Complete the function below.
@qtimer.timeit
def arrangeStudents(a, b):
    def weaveStudents(a, b):
        for i, j in zip(sorted(a), sorted(b)):
            yield i
            yield j

    last = 0
    for student in weaveStudents(a, b):
        if student < last:
            last = 0
            for student in weaveStudents(b, a):
                if student < last:
                    return "NO"
                last = student
            return "YES"
        last = student
    return "YES"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        a = list(map(int, input().rstrip().split()))

        b = list(map(int, input().rstrip().split()))

        result = arrangeStudents(a, b)

        fptr.write(result + '\n')

    fptr.close()

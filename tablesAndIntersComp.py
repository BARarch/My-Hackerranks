#!/Users/anthonyquivers/anaconda3/bin/python
#Date Started: 200929

import math
import os
import random
import re
import sys
import qtimer


# Complete the function below.
@qtimer.timeit
def count_a_probability(chars, N, K):
    combs = list(combinations(chars, K))
    print(len(list(filter(lambda x: 'a' in x, combs))) / len(combs))


if __name__ == "__main__":
    from itertools import combinations
    N = int(input())
    chars = input().split(" ")
    K = int(input())

    count_a_probability(chars, N, K)

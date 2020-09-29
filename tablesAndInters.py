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
    nCombinations = 0
    nAInCombination = 0
    for combination in combinations(chars, K):
        nCombinations += 1
        if 'a' in combination:
            nAInCombination += 1

    combs = list(combinations(chars, K))
    print(len(list(filter(lambda x: 'a' in x, combs)) / len(combs)))
    print(nAInCombination / nCombinations)


if __name__ == "__main__":
    from itertools import combinations
    N = int(input())
    chars = input().split(" ")
    K = int(input())

    count_a_probability(chars, N, K)
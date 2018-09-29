#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import combinations
# Complete the acmTeam function below.
def acmTeam(topic):
    scores = {}
    for pair in combinations(topic, 2):
        score = len(list(filter(lambda x: x == '1', str(bin(int(pair[0], 2) | int(pair[1], 2))))))
        
        if score in scores:
            scores[score] += 1
        else:
            scores[score] = 1
    high = max(scores)
    return [high, scores[high]]
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    topic = []

    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)

    result = acmTeam(topic)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

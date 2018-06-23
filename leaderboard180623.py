#!/bin/python3

import os
import sys

#
# Complete the climbingLeaderboard function below.
#

    


# Complete the climbingLeaderboard function below.
def place_in_list(liss, start, stop, score):
    if (stop - start) <= 1:
        if liss[start] <= score:
            return start
        else:
            return start + 1
        
    mid = (stop + start) // 2
    if liss[mid] == score:
        return mid
    elif liss[mid] > score:
        ## right half
        return place_in_list(liss, mid + 1, stop, score)
    else:
        ## left half liss[mid] < score
        return place_in_list(liss, start, mid, score)
        
    

def climbingLeaderboard(scores, alice):
    result = []  ## Result is a list with m integers denoting the rank for the jth game
    
    ## assign rankings to scores
    rank = 0
    prevScore = -1
    ranks = []
    for score in scores:
        if score == prevScore:
            ranks.append(rank)
        else:
            rank += 1
            ranks.append(rank)
        prevScore = score
        
    ## Find the ranking for Alices Score and append to result
    PIL = -1
    
    for al in alice:
        if PIL != -1:
            PIL = place_in_list(scores, 0, PIL, al)
        else:
            PIL = place_in_list(scores, 0, len(scores), al)
        if PIL == len(ranks):
            result.append(ranks[-1] + 1)
        else:
            result.append(ranks[PIL])
    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    scores_count = int(input())

    scores = list(map(int, input().rstrip().split()))

    alice_count = int(input())

    alice = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(scores, alice)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

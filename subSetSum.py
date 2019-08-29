#!/Users/anthonyquivers/anaconda3/bin/python
#Date Started: 190829

import math
import os
import random
import re
import sys

# Complete the howManyGames function below.
def howManyGames(p, d, m, s):
    # Return the number of games you can buy
    gamesPurchased = 0

    cost = p
    s -= cost

    while s >= 0:
        gamesPurchased += 1
        #print('purchase price: ' + str(cost))     
        cost -= d
        if cost < m:
            cost = m           

        s -= cost

    return gamesPurchased

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    pdms = input().split()

    p = int(pdms[0])

    d = int(pdms[1])

    m = int(pdms[2])

    s = int(pdms[3])

    answer = howManyGames(p, d, m, s)

    fptr.write(str(answer) + '\n')

    fptr.close()

#!/Users/anthonyquivers/anaconda3/bin/python
#Date Started: 190723

import os
import sys

#
# Complete the truckTour function below.
#
def truckTour(petrolpumps):
    #
    # Write your code here.
    #
    
    fuel = 0
    started = 0
    index = 0
    for pump in petrolpumps:
        if fuel < 0:
            started = index
            fuel = 0

        fuel += pump[0] - pump[1]
        index += 1
    
    return started

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    petrolpumps = []

    for _ in range(n):
        petrolpumps.append(list(map(int, input().rstrip().split())))

    result = truckTour(petrolpumps)

    fptr.write(str(result) + '\n')

    fptr.close()
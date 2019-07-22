#!/Users/anthonyquivers/anaconda3/bin/python
#Date Started: 190722

import os
import sys

#
# Complete the truckTour function below.
#
def truckTour(petrolpumps):
    #
    # Write your code here.
    #

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    petrolpumps = []

    for _ in range(n):
        petrolpumps.append(list(map(int, input().rstrip().split())))

    result = truckTour(petrolpumps)

    fptr.write(str(result) + '\n')

    fptr.close()

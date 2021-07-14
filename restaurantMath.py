import math
import os
import random
import re
import sys
import qtimer

@qtimer.timeit
def restaurant(l, b):
    print(f'l = (l), b = {b}')
    if l > b:
        larger, smaller = l, b
    else:
        larger, smaller = b, l
    
    gcd = smaller
    while gcd > 1:
        if smaller % gcd == 0 and larger % gcd == 0:
            return (smaller // gcd) * (larger // gcd)
        gcd -= 1

    return larger * smaller

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        l = int(first_multiple_input[0])

        b = int(first_multiple_input[1])

        result = restaurant(l, b)

        fptr.write(str(result) + '\n')

    fptr.close()
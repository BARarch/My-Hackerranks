#!/Users/anthonyquivers/anaconda3/bin/python
#Date Started: 190720

import os
import sys

#
# Complete the downToZero function below.
#
def downToZero(n):
    #
    # Write your code here.
    #
    from queue import Queue
    from math import sqrt

    def largest_factors(n, step):
        minn = n       
        for i in reversed(range(2, 1 + int(sqrt(n)))):
            if n % i == 0:
                minn = n // i
                yield((minn, step + 1))
        yield((n - 1), step + 1)
        

    #print(list(largest_factors(49, 0)))

    ## I have a largest_factors function that creates an iterator for each child value of n
    ## I add to the queue of itterators for each try
    nValueQ = Queue()
    if n == 0:
        return 0
    nValueQ.put(largest_factors(n, 0))
    visitedFactors = {}
    
    while not nValueQ.empty():
        factors = nValueQ.get_nowait()
        for factor in factors:
            if factor[0] == 2:
                return factor[1] + 2
            if factor[0] == 1:
                return factor[1] + 1
            if factor[0] == 0:
                return factor[1]
    
            if factor[0] not in visitedFactors:
                visitedFactors[factor[0]] = factor[1]
                nValueQ.put(largest_factors(*factor))
                #print(nValueQ.qsize())

    return "Out of Solns"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        n = int(input())
        result = downToZero(n)
        fptr.write(str(result) + '\n')

    fptr.close()

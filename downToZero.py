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

    def largest_factors(n):
        minn = n
        for i in range(2, n):
            if i >= minn:
                break
            if n % i == 0:
                minn = n // i
                yield(minn)

    print(list(largest_factors(7)))
    return 1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    #for q_itr in range(q):
    n = int(input())

    result = downToZero(n)

    fptr.write(str(result) + '\n')

    fptr.close()

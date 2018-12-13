import os
import sys

# Complete the solve function below.

class Fibs:
    def __init__(self):
        self.last = 0
        self.secondToLast = 1
        self.fibs = [0, 1]

    def extend(self, n):
        while n > self.last:
            nextt = self.last + self.secondToLast
            self.fibs.append(nextt)
            self.secondToLast = self.last
            self.last = nextt
        if n in self.fibs:
            return 'IsFibo'
        return 'IsNotFibo'

def solve(n, fo):
    return fo.extend(n)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())
    fibsObject = Fibs()

    for t_itr in range(t):
        n = int(input())
        
        result = solve(n, fibsObject)

        fptr.write(result + '\n')

    fptr.close()

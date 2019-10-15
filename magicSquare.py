#!/Users/anthonyquivers/anaconda3/bin/python
#Date Started: 191013

#!/bin/python3

import sys

def formingMagicSquare(s):
    magicSquares = [[[8,1,6], [3,5,7], [4,9,2]],
                    [[6,1,8], [7,5,3], [2,9,4]],
                    [[4,9,2], [3,5,7], [8,1,6]],
                    [[2,9,4], [7,5,3], [6,1,8]],
                    [[8,3,4], [1,5,9], [6,7,2]],
                    [[4,3,8], [9,5,1], [2,7,6]],
                    [[6,7,2], [1,5,9], [8,3,4]],
                    [[2,7,6], [9,5,1], [4,3,8]]]
    def compare(s):
        def fun(x):
            summ = 0
            for rowI, rowJ in zip(s, x):
                for i, j in zip(rowI, rowJ):
                    summ += abs(i - j)
            return summ
        return fun
    res = list(map(compare(s), magicSquares))
    a = min(res)
    print(res.index(a))    
    return a

if __name__ == "__main__":
    s = []
    for s_i in range(3):
       s_t = [int(s_temp) for s_temp in input().strip().split(' ')]
       s.append(s_t)

    print(s)
    result = formingMagicSquare(s)
    print(result)

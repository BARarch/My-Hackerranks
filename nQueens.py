#!/Users/anthonyquivers/anaconda3/bin/python
#Date Started: 191019

def nQueens(n):
    # What is a viable solution for each colunm and colunm value:
    #   Positions not in the right, up, and down sets
    # What is the rejection criteria, how do we implement it?
    #   Pruning, modify the right, up, and down, sets at each level
    #   and difference them from the set of all posible positions
    def nQueensHelp(n, viable, right, up, down):
        # That prune set has three components right, up, and down
        if len(viable) == n:
            return [viable, ]
        solns = []
        viables = {x for x in range(1, n + 1)} - (right | up | down) 
        for x in viables:
            solns += nQueensHelp(   n, 
                                    viable + [x, ], 
                                    right | {x}, 
                                    {y - 1 for y in up} | {x - 1}, 
                                    {y + 1 for y in down} | {x + 1}) 
        return solns

    return list(sorted(nQueensHelp(n, [], {0}, {0}, {n + 1})))

if __name__ == '__main__':
    import os
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    print("n: {}".format(n))

    fptr.write(str(nQueens(n)))
    fptr.write('\n')

    fptr.close()
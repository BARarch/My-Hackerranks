#!/Users/anthonyquivers/anaconda3/bin/python
#Date Started: 200328
def graphDistances(g, s):
    infinity = 31 

    def weight(i, j):
        return g[i][j]

    def find_mininum(g, selected, remaining, distances):
        minn = (None, infinity)
        for v in remaining:
            if weight(selected, v) <= minn[1]:
                minn = (v, weight(selected, v))
        return minn

    #Edit diagonals from -1 to 0
    for c, row in enumerate(g):
        if row[c] == -1:
            row[c] = 0

    g[s][s] = 0

    # Edit non-links in matrix from -1 to infinity value
    for i, row in enumerate(g):
        for j, val in enumerate(row):
            if g[i][j] == -1:
                g[i][j] = infinity

    S = set([s,])
    R = set(range(len(g))).difference(S) # Set of remainging vortexies
    selected = s
    
    d = g[s]

    addedDistance = 0
    while R:
        # Update values for distances
        s, w = find_mininum(g, s, R, d)
        addedDistance += w
        S.add(s)
        R = R.difference(S)
        for v in R:
            d[v] = min(d[v], addedDistance + weight(s, v))


    return d




if __name__ == '__main__':
    import os
    from cs_utils import *
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    l = list_string_to_list(input())
    #ll = list_string_to_linked_list(input())
    i = int(input())
    #s = input()

    fptr.write(str(graphDistances(l, i)))
    fptr.write('\n')

    fptr.close()

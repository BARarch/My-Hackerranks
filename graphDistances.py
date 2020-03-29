#!/Users/anthonyquivers/anaconda3/bin/python
#Date Started: 200328
def graphDistances(g, s):
    infinity = "inf"

    def weight(i, j):
        return g[i][j]

    def find_mininum(g, selected, remaining, distances):
        minn = (None, 31)
        for v in remaining:
            if distances[v] != 'inf':
                if distances[v] <= minn[1]:
                    minn = (v, distances[v])
        return minn

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

    '''
    for row in g:
        print("\t" * 2 + "\t".join(map(str, row)))
    print("selected |  \t" + "\t".join(map(str, range(len(g)))))
    print("------------" + "--------" * len(g) )
    print(" " + str(s) + " \t |  \t" + "\t".join(map(str, d)), end='\t')
    '''
    while R:
        # Update values for distances
        s, w = find_mininum(g, s, R, d)
        S.add(s)
        R = R.difference(S)
        #print("min:\t" + str(w) + "\tadded:  "+ str(w))
        for v in R:
            current = d[v]
            weightFromSelected = weight(s, v)
            if current == 'inf':
                if weightFromSelected != 'inf':
                    d[v] = w + weightFromSelected
            elif weightFromSelected != 'inf':
                d[v] = min(current, w + weightFromSelected)
    '''                
        print(" " + str(s) + " \t |  \t" + "\t".join(map(str, d)), end='\t')

    print()  
    '''
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

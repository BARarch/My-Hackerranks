from collections import deque

def steps(d, n, pt):
    # Iterator that computes the next steps from a point
    # These use translated coordinates
    a = pt[:]
    for dim, i, in enumerate(pt):
        if (i + 2) < n:
            a[dim] = i + 2
            yield a[:]

        a[dim] = abs(i - 2)
        yield a[:]
        a[dim] = i


        

def translatePoint(d, n, pt):
    ## Shift coodinates to center of grid for even n
    return [abs((2 * (x - int(n / 2))) + 1) for x in pt]

def gridWalks(d, n, m, start):
    # This is a dynamic programming technique to find the number of valid walks
    # Do only a quadrant
    # for even n there are n/2 lines numbered 1 to n - 1 numbered in increments of 2
    # for instance if n = 10 the 5 lines for the quadarant will be 1, 3, 5, 7, and 9
    #print("{}, {}".format(start, m))
    #print(H)
    if m == 0:
        return 1

    walks = 0
    spt = tuple(sorted(start))
    if spt in H:
        if m in H[spt]:
            return H[spt][m]
    
    # Does all the work
    for step in steps(d, n,start):
        #print()
        walks += gridWalks(d, n, m - 1, step)

    # Hashing for memoization
    if spt in H:
        H[spt][m] = walks
    else:
        H[spt] = {m: walks}

    return walks




if __name__ == "__main__":
    # The description case: d = 2, m = 3, n = 2
    # This script only works in even m so I changed it to 4 to test
    H = {}
    print("\nd = 2, n = 4, m = 2 to Check")
    print('Corner: Should be 6' )
    pt = translatePoint(2, 4, [0, 0])
    print(gridWalks(2, 4, 2, pt))

    print('\nCenter: Should be 14') 
    pt = translatePoint(2, 4, [2, 2])
    
    print(gridWalks(2, 4, 2, pt))
    print("Hashes: " + str(len(H)))

    # Problem 1
    H = {}
    D = 4
    N = 10
    M = 10
    print("\nd = 4, n = 10, m = 10")
    print('Corner: Problem 1')
    pt = translatePoint(D, N, [0, 0, 0, 0])
    NwalksCorner  = gridWalks(D, N, M, pt)
    print(NwalksCorner)

    print('\nCenter') 
    pt = translatePoint(D, N, [5, 5, 5, 5])
    print(gridWalks(D, N, M, pt))

    ## Problem 2 and 3
    import numpy as np
    from itertools import product
    print('\nFull Distribution: Problems 2 and 3')
    dist = list(map(lambda x: gridWalks(D, N, M, list(x)), product(range(1, N, 2), repeat=D)))
    arr = np.array(dist)
    #print(dist)
    print("Min: {}".format(arr.min()))
    print("Max: {}".format(arr.max()))
    print("\nThe Ratio: ")
    print(arr.max() / arr.min())
    print("\nStandard Devation to Mean")
    print(arr.std() / arr.mean())
    print("Hashes: {}".format(len(H)))

    H = {}
    D = 8
    N = 12
    M = 12
    ## Problem 4
    print("\nd = 8, n = 12, m = 12")
    print('Corner: Problem 4')
    pt = translatePoint(D, N, [0, 0, 0, 0, 0, 0, 0, 0])
    print(gridWalks(D, N, M, pt))

    print("\nCenter")
    pt = translatePoint(D, N, [6, 6, 6, 6, 6, 6, 6, 6])
    print(gridWalks(D, N, M, pt))

    
    ## Problem 5 and 6
    print('\nFull Distribution: Problems 5 and 6')
    dist = list(map(lambda x: gridWalks(D, N, M, list(x)), product(range(1, N, 2), repeat=D)))
    arr = np.array(dist)
    #print(dist)
    print("Min: {}".format(arr.min()))
    print("Max: {}".format(arr.max()))
    print("\nThe Ratio: ")
    print(arr.max() / arr.min())
    print("\nStandard Devation to Mean")
    print(arr.std() / arr.mean())
    print("Hashes: {}".format(len(H)))
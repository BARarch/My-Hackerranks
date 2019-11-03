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
    H = {}
    #print(translatePoint(4, 10, [5, 5, 5, 5]))
    #print(list(steps(4, 10, [9 ,9,9,9])))

    #pt = translatePoint(8, 12, [6, 6, 6, 6, 6, 6, 6, 6,])
    #print(gridWalks(8, 12, 12, pt))

    H = {}
    print("\nd = 2, n = 4, m = 2")
    print('Corner')
    pt = translatePoint(2, 4, [0, 0])
    print(pt)
    print(gridWalks(2, 4, 2, pt))

    print('\nCenter') 
    pt = translatePoint(2, 4, [2, 2])
    print(pt)
    print(gridWalks(2, 4, 2, pt))
    print("Hases: " + str(len(H)))

    H = {}
    print("\nd = 4, n = 10, m = 10")
    print('Corner')
    pt = translatePoint(4, 10, [0, 0, 0, 0])
    print(gridWalks(4, 10, 10, pt))

    print('\nCenter') 
    pt = translatePoint(4, 10, [5, 5, 5, 5])
    print(gridWalks(4, 10, 10, pt))
    print("Hases: " + str(len(H)))

    H = {}
    print("\nd = 8, n = 12, m = 12")
    print("Corner")
    pt = translatePoint(8, 12, [0, 0, 0, 0, 0, 0, 0, 0])
    print(gridWalks(8, 12, 12, pt))

    print("\nCenter")
    pt = translatePoint(8, 12, [6, 6, 6, 6, 6, 6, 6, 6])
    print(gridWalks(8, 12, 12, pt))

    print("Hases: " + str(len(H)))
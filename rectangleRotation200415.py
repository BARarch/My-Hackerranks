def rectangleRotation(a, b):
    from math import sqrt
    d = sqrt(2) / 2

    # compute x1:
    x1 = 1 + 2 * ((b / 2) // (2 * d))

    pts = x1

    # compute x2:
    x2 = 0
    while (d + (x2 * (2 * d))) < (b / 2):
        x2 += 1    
    x2 *= 2

    #print("x1: " + str(x1))
    #print("x2: " + str(x2))

    n = 1
    while (n * d) < (a / 2):
        if n % 2 == 1:
            ## odd n, use x2
            pts += 2 * x2
        else:
            ## even n use x1
            pts += 2 * x1
        n += 1

    #print("n: ", str(n - 1))

    return pts 

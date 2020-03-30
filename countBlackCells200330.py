def countBlackCells(n, m):
    import math
    from itertools import count
    val = map(lambda x: x * n / m, count())

    y_0 = next(val)
    blackCells = 0

    for x_0 in range(m):
        start = math.ceil(y_0) - 1
        if x_0 == 0:              ## Override if First colum
            start = 0

        y_1 = next(val)
        stop = math.floor(y_1) + 1 ## val = 78.4 stop =79
        if x_0 + 1 == m:           ## Override if last colunm
            stop = n 

        y_0 = y_1
        blackCells += stop - start

    return blackCells





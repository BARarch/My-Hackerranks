def secondRightmostZeroBit(n):
    return list(filter(lambda x: (n // x % 2 == 0), map(lambda y: 2 ** y, range(30))))[1]

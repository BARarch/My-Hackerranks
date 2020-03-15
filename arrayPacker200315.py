def arrayPacking(a):
    res = 0
    shift = 0

    for n in a:
        addr = n << shift
        res += addr
        shift += 8

    return res



def mirrorBits(a):
    exp = 1
    res = 0
    for dig in bin(a)[2:]:
        if dig == '1':
            res += exp
        exp *= 2

    return res


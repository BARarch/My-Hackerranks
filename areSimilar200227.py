def areSimilar(a, b):
    c = None
    d = None

    for i, num in enumerate(a):
        if b[i] != num:
            if c == None:
                c = (i, num)
            elif d == None:
                d = (i, num)
            else:
                return False

    if c == None and d == None:
        return True

    if c == None and d != None:
        return False
        
    if d[1] == b[c[0]] and c[1] == b[d[0]]:
        return True
    else:
        return False


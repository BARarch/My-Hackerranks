def increaseNumberRoundness(n):
    foundZero = False
    
    for c in str(n):
        if foundZero:
            if c is not '0':
                return True
        else:
            if c is '0':
                foundZero = True

    return False



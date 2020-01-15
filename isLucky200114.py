def isLucky(n):
    stringN = str(n)
    a = stringN[:(len(stringN) // 2)]
    b = stringN[(len(stringN) // 2):]
    
    sumA = 0
    for i in a:
        sumA += int(i)
        
    sumB = 0
    for i in b:
        sumB += int(i)
        
    return sumA == sumB

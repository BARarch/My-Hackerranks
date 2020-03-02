def palindromeRearranging(inputString):
    charCount = {}
    for c in inputString:
        if c in charCount:
            charCount[c] += 1
        else:
            charCount[c] = 1

    nOdd = 0
    for count in charCount.values():
        if (count % 2) != 0:
            nOdd += 1
        if nOdd > 1:
            return False
    
    return True


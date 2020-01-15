def allLongestStrings(inputArray):
    longestLength = 0
    longStrings = []
    for s in inputArray:
        if len(s) == longestLength:
            longStrings.append(s)
        elif len(s) > longestLength:
            longStrings = [s, ]
            longestLength = len(s)
            
    return longStrings

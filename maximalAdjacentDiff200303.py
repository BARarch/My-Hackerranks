def arrayMaximalAdjacentDifference(inputArray):
    prev = None
    maxDiff = 0 

    for num in inputArray:
        if prev is None: 
            prev = num
        else:
            if abs(prev - num) > maxDiff:
                maxDiff = abs(prev - num)
            prev = num

    return maxDiff


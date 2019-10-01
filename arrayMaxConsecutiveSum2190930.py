def arrayMaxConsecutiveSum2(inputArray):
    #[-2, 2, 5, -11, 6]
    #[-2, 0, 5, -6, 0]

    #[-3, -2, -1, -4]
    #[-3, -5, -6, -10]
    
    #[1, -2, 3, -4, 5, -3, 2, 2, 2]
    #[1, -1, 3, -1, 4,  1, 3, 5, 7] <= Max Sum - Min Sum
    
    #[11, -2, 1, -4, 5, -3, 2, 2, 2]
    #[11, 9, 10, 6, 11, 8, 10, 12, 14]
    
    bigSum = [0, ]
    conSum = 0
    maxSum = inputArray[0]
    maxSumLoc = 1
    minSum = 0
    increase = 0
    
    for i, num in enumerate(inputArray):
        conSum += num
        increase += num
        if conSum < minSum:
            print("Min Sum {} at i = {}".format(conSum, i))
            minSum = conSum
            increase = 0
            
        if increase > maxSum:
            maxSum = increase
            print("Max Sum {} at i = {}".format(conSum, i))
            #maxSumLoc = i + 1
        
        #bigSum.append(conSum)
     
    if maxSum == 0:
        return max(inputArray)
    return maxSum
    
    

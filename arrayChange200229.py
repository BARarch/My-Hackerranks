def arrayChange(inputArray):
    greaterThan = inputArray[0]
    moves = 0 
    for i in inputArray:
        if i >= greaterThan:
            greaterThan = i + 1
        else:
            moves += greaterThan - i
            # New Value for i is i + greaterThan - i + 1
            greaterThan = greaterThan + 1
            
    return moves
            


def matrixElementsSum(matrix):
    summ = 0
    hauntedNumber = []
    for i, row in enumerate(matrix):
        for roomNumber, cost in enumerate(row):
            if roomNumber not in hauntedNumber:
                if cost == 0:
                    hauntedNumber.append(roomNumber)
                summ += cost
                
    return summ

def flippingMatrix(matrix):
    n = len(matrix) // 2
    def transpose(matrix):
        trans = [[0, ] * len(matrix)] * len(matrix)
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                trans[i][j] = matrix[j][i]
        return trans
    
    swaps = 1
    
    while swaps > 0:
        swaps = 0
        ## Algoriz
        # Compare Rows in quadrants 3 and 4
        for row in matrix[n:]: ## Bottom Half
            if sum(row[:n]) > sum(row[n:]):
                row.reverse()
                swaps += 1
                
        # Transposed to Compare Colunms in quadrants 2 and 4 now
        matrix = transpose(matrix)
        for row in matrix[n:]: ## Bottom Half
            if sum(row[n:]) > sum(row[:n]):
                row.reverse()
                swaps += 1
                
        # Transpose it back to Compare the rows of quadrants 1 and 2
        matrix = transpose(matrix)
        for row in matrix[:n]: ## Top Half
            if sum(row[n:]) > sum(row[:n]):
                row.reverse()
                swaps += 1
         
                
    res = 0
    for row in matrix[:n]:
        res += sum(row[:n])
    
    return res


    ''' Input
    1
    2
    112 42 83 119
    56 125 56 49
    15 78 101 43
    62 98 114 108 
    '''
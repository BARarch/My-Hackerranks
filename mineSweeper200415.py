def minesweeper(matrix):
    def mineCount(matrix, row, col):
        count = 0
        #print("row: " + str(row) + " col: " + str(col))
        for r in range(max(0, row - 1), min(len(matrix), row + 2)):
            for c in range(max(0, col - 1), min(len(matrix[row]), col + 2)):
                #print((r, c), end=" ")
                if matrix[r][c] and (r, c) != (row, col):
                    count += 1

        #print()
        return count

    res = []
    for r in range(len(matrix)):
        rowRes = []
        for c in range(len(matrix[r])):
            rowRes.append(mineCount(matrix, r, c))
        
        res.append(rowRes)

    return res


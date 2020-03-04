def seatsInTheater(nCols, nRows, col, row):
    rowsInBack = nRows - row
    colsInBack = nCols - col + 1

    return rowsInBack * colsInBack

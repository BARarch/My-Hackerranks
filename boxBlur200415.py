def boxBlur(image):
    def avg(image, r, c):
        summ = image[r - 1][c - 1]
        summ += image[r - 1][c]
        summ += image[r - 1][c + 1]
        summ += image[r][c - 1]
        summ += image[r][c]
        summ += image[r][c + 1]
        summ += image[r + 1][c - 1]
        summ += image[r + 1][c]
        summ += image[r + 1][c + 1]

        return summ // 9

    res = []
    for row in range(1,len(image) - 1):
        resRow = []
        for col in range(1,len(image[0]) - 1):
            resRow.append(avg(image, row, col))

        res.append(resRow)

    return res



def rangeBitCount(a, b):
    def countOnes(x):
        ones = 0
        for i in bin(x)[2:]:
            if i == "1":
                ones += 1

        return ones

    totalOnes = 0

    for curr in range(a, b + 1):
        totalOnes += countOnes(curr)

    return totalOnes




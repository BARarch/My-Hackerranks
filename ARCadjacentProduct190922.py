def adjacentElementsProduct(inputArray):
    a = inputArray[:len(inputArray) - 1]
    b = inputArray[1:]
    return max(map(lambda x: x[0] * x[1], zip(a, b)))

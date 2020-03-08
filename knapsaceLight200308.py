def knapsackLight(value1, weight1, value2, weight2, maxW):
    maxCarry = 0

    if weight1 <= maxW:
        maxCarry = value1

    if weight2 <= maxW:
        if value2 > maxCarry:
            maxCarry = value2
        
    if (weight1 + weight2) <= maxW:
        return value1 + value2

    return maxCarry


def shapeArea(n):
    area = 0
    
    for i in range(n):
        if i == 0:
            area += 1
        else:
            area += 4 * i

    return area

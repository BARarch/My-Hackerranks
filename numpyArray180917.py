import numpy

def arrays(arr):
    # complete this function
    # use numpy.array
    return numpy.array(list(reversed(arr)), float)

arr = input().strip().split(' ')
result = arrays(arr)
print(result)

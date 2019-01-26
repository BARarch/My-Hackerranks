import numpy

numpy.set_printoptions(sign=' ')

arr = numpy.array(list(map(float, input().strip().split(' '))))

print(numpy.floor(arr))
print(numpy.ceil(arr))
print(numpy.rint(arr))

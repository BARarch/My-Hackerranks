import numpy

dims = tuple(map(int, input().strip().split(' ')))
print(numpy.zeros(dims, dtype=numpy.int))
print(numpy.ones(dims, dtype=numpy.int))

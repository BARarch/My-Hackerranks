import numpy

numpy.set_printoptions(legacy='1.13')
N, M = tuple(map(int, input().strip().split(' ')))
print(numpy.eye(N, M, k=0))

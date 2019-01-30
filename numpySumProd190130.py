import numpy
N, M = tuple(map(int, input().strip().split(' ')))

print(numpy.prod(numpy.array(numpy.sum(numpy.array([list(map(int, input().strip().split(' '))) for _ in range(N)]), axis=0))))

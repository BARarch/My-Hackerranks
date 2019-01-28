import numpy
numpy.set_printoptions(legacy='1.13')

N, M = tuple(map(int, input().split(' ')))

arr = numpy.array([list(map(int, input().strip().split(' '))) for _ in range(N)])

print(numpy.mean(arr, axis=1))
print(numpy.var(arr, axis=0))
print(numpy.std(arr))


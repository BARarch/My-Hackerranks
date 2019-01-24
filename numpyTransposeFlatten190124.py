import numpy

N, M = tuple(map(int, input().strip().split(' ')))

arr = numpy.array([list(map(int, input().strip().split(' '))) for _ in range(N)])

print(arr.transpose())
print(arr.flatten())


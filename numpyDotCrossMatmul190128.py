import numpy

N = int(input().strip())

A = numpy.array([list(map(int, input().strip().split(' '))) for _ in range(N)])
B = numpy.array([list(map(int, input().strip().split(' '))) for _ in range(N)])

print(numpy.matmul(A, B))

[3;2~import numpy

N, M = tuple(map(int, input().strip().split(' ')))

a = numpy.array([list(map(int, input().strip().split(' '))) for _ in range(N)])
b = numpy.array([list(map(int, input().strip().split(' '))) for _ in range(N)])

print(a + b)
print(a - b)
print(a * b)
print(a // b)
print(a % b)
print(a ** b)

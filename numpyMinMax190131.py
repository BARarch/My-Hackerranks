import numpy

print(max(numpy.min(numpy.array([list(map(int, input().split(' '))) for _ in range(int(input().split(' ')[0]))]), axis=1)))

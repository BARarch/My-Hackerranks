#import numpy
#import scipy
import math

N = int(input())
vals = list(map(int, input().split(' ')))

mean = sum(vals) / len(vals)
var = sum(map(lambda x: (x - mean) ** 2, vals)) / len(vals)

print(round(math.sqrt(var), 1))

# Enter your code here. Read input from STDIN. Print output to STDOUT
from functools import reduce
from operator import add, mul

N = int(input())
vals = list(map(int, input().split(' ')))
weights = list(map(int, input().split(' ')))
 
print(round(reduce(add, map(lambda x: reduce(mul, x), zip(vals, weights))) / reduce(add, weights), 1))

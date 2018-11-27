# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np
from scipy import stats

N = int(input())
vals = list(map(int, input().split(' ')))

print(np.mean(vals))
print(np.median(vals))
print(stats.mode(vals)[0][0])

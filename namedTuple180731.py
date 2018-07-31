from collections import namedtuple
N = int(input())
row = namedtuple('row', (lambda x, n: [x[i:i+n].strip() for i in range(0, len(x), n)])(input().strip(), 10))
print(sum([float(row._make((lambda x, n: [x[i:i+n].strip() for i in range(0, len(x), n)])(input().strip(),10)).MARKS) for i in range(N)]) / N)

##mullArray
from operator import mul
from functools import reduce
if __name__ == "__main__":
    L = [4,3,2]
    print(reduce(mul, L))

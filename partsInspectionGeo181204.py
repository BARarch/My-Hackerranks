1 3
[D[A[C[Cdef prob(a, b):
    return a / (a + b)

def probFraction(a, b):
    return a / b

def fact(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    return n * fact(n - 1)

def nChooseK(n, k):
    return fact(n) / (fact(k) * fact(n - k))

def binomialProb(x, n, p):
    return nChooseK(n, x) * (p ** (x)) * ((1 - p) ** (n - x))

def geoProb(n, p):
    return ((1 - p) ** (n - 1)) * p

if __name__ == "__main__":
    a, b = tuple(map(float, input().split(' ')))
    #print(a)
    #print(b)
    p = probFraction(a, b)
    n = int(input())

    print(round(geoProb(n, p), 3))

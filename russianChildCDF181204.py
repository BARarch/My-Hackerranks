[3;2~def prob(a, b):
    return a / (a + b)

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

if __name__ == "__main__":
    a, b = tuple(map(float, input().split(' ')))
    #print(a)
    #print(b)
    p = prob(a, b)
    n = 6
    prob = 0.0
    for x in range(3,7):
        prob += binomialProb(x, n, p)

    print(round(prob, 3))

from math import exp

def fact(n):
    if n == 1 or n == 0:
        return 1
    return n * fact(n - 1)

def poisson(k, l):
    return (l ** k) * exp(-l) / fact(k)
    

if __name__ == '__main__':
    l = float(input())
    x = float(input())

    print(poisson(x, l))

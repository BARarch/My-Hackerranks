from math import sqrt

def std(x):
    vals = x
    mean = avg(x)
    return sqrt(sum(map(lambda x: (x - mean) ** 2, vals)) / len(vals))

def avg(x):
    return sum(x) / len(x)

if __name__ == '__main__':
    n = int(input())
    #print(input())
    #print(input())

    X = list(map(float, input().rstrip().split(' ')))
    Y = list(map(float, input().rstrip().split(' ')))
    #print(X)
    #print(Y)

    mX = avg(X)
    oX = std(X)

    mY = avg(Y)
    oY = std(Y)

    cc = sum([(x - mX) * (y - mY) for x, y in zip(X, Y)]) / (n * oY * oX)
    print(round(cc, 3))

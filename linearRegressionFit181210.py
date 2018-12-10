from math import sqrt
#from sklearn import linear_model
#import numpy as np

def std(x):
    vals = x
    mean = avg(x)
    return sqrt(sum(map(lambda x: (x - mean) ** 2, vals)) / len(vals))

def avg(x):
    return sum(x) / len(x)

def pcc(X, Y):
    mX = avg(X)
    oX = std(X)

    mY = avg(Y)
    oY = std(Y)

    return sum([(x - mX) * (y - mY) for x, y in zip(X, Y)]) / (n * oY * oX)

if __name__ == "__main__":
    n = 5
    
    scores = [tuple(map(float, input().rstrip().split(' '))) for _ in range(n)]
    #print(scores)
    X = list(map(lambda x: x[0], scores))
    Y = list(map(lambda x: x[1], scores))

    b = pcc(X, Y) * (std(Y) / std(X))
    a = avg(Y) - (b * avg(X))

    ans = a + (b * 80)
    print(round(ans, 3))

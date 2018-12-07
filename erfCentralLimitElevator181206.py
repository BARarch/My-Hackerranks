from math import erf, sqrt

def cdf(x, u, o):
    ''' u: mean
        o: standard deviation
    '''
    return (1 / 2) * (1 + erf((x - u) / (o * sqrt(2))))

if __name__ == "__main__":
    maxWieght = float(input())
    n = int(input())
    mean = float(input())
    stDev = float(input())

    print(round(cdf(maxWieght, n * mean, sqrt(n) * stDev ), 4))

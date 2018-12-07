from math import sqrt

if __name__ == "__main__":
    n = int(input())
    mean = float(input())
    stDev = float(input())
    interval = float(input())
    z = float(input())

    print(round(mean - (stDev * z / sqrt(n)), 2))
    print(round(mean + (stDev * z / sqrt(n)), 2))

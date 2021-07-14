import math

def constructShell(n):
    return [[0 for _ in range(n - abs(x))] for x in range(-n + 1, n)]


if __name__ == "__main__":
    n = 5
    for row in constructShell(n):
        print(row)
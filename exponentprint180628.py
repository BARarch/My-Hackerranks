import math

if __name__ == '__main__':
    n = int(input())
    exp = 0
    summ = 0
    while n > 0:
        summ += n * (10 ** exp)
        exp += 1 + int(math.log10(n))
        n -= 1
        
    print(summ)

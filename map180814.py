cube = lambda x: x ** 3 # complete the lambda function 

def fibonacci(n):
    if n == 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fibs = fibonacci(n - 1)
        fibs.append(fibs[-1] + fibs[-2])
        return fibs
if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))

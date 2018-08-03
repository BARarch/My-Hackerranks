N = int(input())

for _ in range(N):
    try:
        a, b = map(int ,input().split(' '))
        print(a // b)
    except ZeroDivisionError as e:
        print('Error Code: {}'.format(e))
    except ValueError as e:
        print('Error Code: {}'.format(e))

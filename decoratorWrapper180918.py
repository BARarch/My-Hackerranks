def modify(num):
    if len(num) == 10:
        return '+91 {} {}'.format(num[:5], num[5:])
    elif num[0] == '0':
        return '+91 {} {}'.format(num[1:6], num[6:])
    elif num[:3] == '+91':
        return '+91 {} {}'.format(num[3:8], num[8:])
    else:
        return '+91 {} {}'.format(num[2:7], num[7:])

def wrapper(f):
    def fun(l):
        f(list(map(modify, l)))
        
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l)

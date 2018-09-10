def lower(ch):
    return ch.islower()

def upper(ch):
    return ch.isupper()

def odd(ch):
    return bool(int(ch) % 2) if ch.isdigit() else False

def even(ch):
    return not bool(int(ch) % 2) if ch.isdigit() else False

s = input()

print(''.join(sorted(filter(lower, s))) + ''.join(sorted(filter(upper, s))) + ''.join(sorted(filter(odd, s))) + ''.join(sorted(filter(even, s))))

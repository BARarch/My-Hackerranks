from itertools import *

n, m = map(int, input().split(' '))
lists = [list(map(int, input().split(' ')[1:])) for _ in range(n)]

def max_mod(lists, mod):
    modulos = list(repeat(0, mod))
    modulos[0] = 1

    for li in lists:
        newMods = list(repeat(0, mod))
        for mo in compress(count(0), modulos):    
            for i in li:
                newMods[(mo + ((i ** 2) % mod)) % mod] = 1
        modulos = newMods

    return list(compress(count(0), modulos))[-1]

print(max_mod(lists, m))

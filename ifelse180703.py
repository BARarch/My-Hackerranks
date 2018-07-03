#!/bin/python3

N = int(input())

if N % 2:
    even = False
else:
    even = True
    
if N >= 2 and N <= 5 and even:
    print('Not Weird')
elif N >= 6 and N <= 20 and even:
    print('Weird')
elif N > 20 and even:
    print('Not Weird')
else:
    print('Weird')

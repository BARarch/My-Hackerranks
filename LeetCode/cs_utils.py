import os
import sys
from collections import deque

def check_for_closed(exp, f):
    for c in exp:
        braq = {'{':'}', '[':']', '(':')'}
        if c in braq:
            f.append(braq[c])
        if f and (c == f[-1]):
            f.pop()
            

def dict_statement_reader(stream):
    ## This is a generator that produces a (var, exp) tuple 
    ## for eached closed expression
    ## we will keep reading lines until all ()s, {}s and []s
    ## of the epressions arer closed.
    sys.stdin = stream

    while True:
        f = deque()
        try:
            vals = input().strip().split(":")
            var = vals[0]
            exp = ": ".join(vals[1:])
            
            check_for_closed(exp, f)
            while not exp or f:
                nextLine = input().strip()
                check_for_closed(nextLine, f)
                exp += nextLine
            
            yield var, exp
        
        except EOFError:
            stream.close()
            break

def dict_statement_reader_native(stream):
    ## This is a generator that produces a (var, exp) tuple 
    ## for eached closed expression
    ## we will keep reading lines until all ()s, {}s and []s
    ## of the epressions arer closed.

    while True:
        f = deque()
        try:
            vals = input().strip().split(":")
            var = vals[0]
            exp = ": ".join(vals[1:])
            
            check_for_closed(exp, f)
            while not exp or f:
                nextLine = input().strip()
                check_for_closed(nextLine, f)
                exp += nextLine
            
            yield var, exp
        
        except EOFError:
            stream.close()
            break
            

if __name__ == "__main__":
    fd = open('dictStringTest.txt')

    for var, exp in dict_statement_reader_native(fd):
        exec(var + " = " + exp)

    print(f'l is {l}')
    print(type(l))
    print(f'r is {r}')
    print(type(r))
    print(f'p is {p}')
    print(type(p))
    print(f's is {s}')
    print(type(s))

    print(f'd is {d}')
    print(type(d))
    print(f'a is {a}')
    print(type(a))
    
    

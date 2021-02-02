import qtimer

@qtimer.timeit
def myfunct(n):
    return fibs(n)

def fibs(n):    
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 1
    return fibs(n - 2) + fibs(n - 1)

if __name__ == '__main__':
    import os
    from cs_utils import *
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    #l = list_string_to_list(input())
    #ll = list_string_to_linked_list(input())
    #i = int(input())
    #s = input()
    n = 40
    print(f"Testing fibs with n = {n}")
    print(myfunct(n))

    #fptr.write(str("Function Call to Return Answer Here"))
    #fptr.write('\n')

    #fptr.close()
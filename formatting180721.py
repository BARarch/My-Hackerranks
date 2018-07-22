def print_formatted(number):
    # your code goes here
    width = len(bin(number)) - 2
    for i in range(number):
        num = i+1
        print('{0: >{4}} {1: >{4}} {2: >{4}} {3: >{4}}'.format(str(num), oct(num)[2:], hex(num)[2:].upper(), bin(num)[2:], width))
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)

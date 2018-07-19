from string import ascii_lowercase

def reflect(string):
    i = 0
    res = []
    while i < len(string):
        i += 1
        res.append(string[-i])       
    i -= 1    
    while i > 0:
        res.append(string[-i])
        i -= 1     
    return res
        
def print_rangoli(size):
    width = ((size - 1) * 4) + 1
    start = size 
    # Top Half
    while start > 0:
        start -= 1
        print("-".join(reflect(ascii_lowercase[start:size])).center(width, '-'))    
    # Bottom Half    
    start += 1
    while start < size:
        print("-".join(reflect(ascii_lowercase[start:size])).center(width, '-'))
        start += 1

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)

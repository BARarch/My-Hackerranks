def palindromeIndex(s):
    
    a = 0
    b = len(s) - 1
    
    while a <= b and s[a] == s[b]:
        a += 1
        b -= 1
        
    if a >= b:
        return -1
        
    res1 = a
    res2 = b
    a += 1
    
    while a <= b and s[a] == s[b]:
        a += 1
        b -= 1
        
    if a >= b:
        return res1
    else:
        return res2
    
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = palindromeIndex(s)

        fptr.write(str(result) + '\n')


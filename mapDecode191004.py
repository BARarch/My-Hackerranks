def mapDecoding(message):
    
    if len(message) == 0:
        return 1
        
    def decodes(c):
        return (int(c) > 0 and int(c) <= 26)
    
    curr = 0
    
    b = None
    lastOne = 1
    lastTwo = 1
    
    for a in reversed(message):
        if a == '0':
            curr = 0
        else:
            curr = lastOne
            if b is not None and decodes(a + b):
                curr += lastTwo
            curr %= 1000000007
        
        lastTwo = lastOne
        lastOne = curr
        b = a
     
        
    return curr
        
            


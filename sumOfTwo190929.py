def sumOfTwo(a, b, v):
    #a = list(sorted(a))
    b = {x: '' for x in b }
    
    for num in a:
        val = v - num
        
        if val in b:
            return True
    
    return False

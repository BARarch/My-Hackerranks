from collections import deque

def reverseInParentheses(inputString):
    def reverseNow(IS):
        res = ''
        a = IS.popleft()
        while a != ")":
            if a == "(":
                res += reverseNow(IS)
            else:
                res += a
            a = IS.popleft()
        
        return ''.join(list(reversed(res)))
        
    IS = deque(inputString)
    res = ''
    while IS:
        a = IS.popleft()
        if a == "(":
            res += reverseNow(IS)
        else:
            res += a
            
    return res
        


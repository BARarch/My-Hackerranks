
class Solution:
    def findBots(self,usernames:List[str],n : int) -> List[int]:
        # code here
        # print("Hello world")
        from collections import deque
        from itertools import count
        from collections import defaultdict
        
        def primeGen():
            table = defaultdict(list)
            for x in count(2):
                facts = table[x]
                if facts:
                    del table[x]
                    for p in facts:
                        table[x+p] = table[x+p] + [p]
                else:
                    table[x*x] = [x]
                    yield x
                    
        def evenPositionsChar(word):
            send = False
            for c in word:
                if send:
                    yield c 
                
                send = not send
        
        prime = primeGen()        
        largestPrime = 0
        primeSet = set() ## Starter Values
                
        def is_prime(n, largestPrime, primeSet):
            while n > largestPrime:
                ## add to primes
                largestPrime = next(prime)
                primeSet.add(largestPrime)
                
            return n in primeSet, largestPrime, primeSet
                
        res = []
                
        for username in usernames:
            H = set()
            nDistinct = 0
            for c in evenPositionsChar(username):
                if c not in H:
                    nDistinct += 1
                    H.add(c)
            
            print(username)
            print(H)
            print(nDistinct)
            isAPrime, largestPrime, primeSet = is_prime(nDistinct, largestPrime, primeSet)
            if isAPrime:
                res.append(1)
            else:
                res.append(0)
            
        print(primeSet)            
        return res
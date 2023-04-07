import string
from collections import deque

if __name__ == "__main__":

    def longestPalindrome( s: str) -> str:
        print(f'\nLongest Palendrom in {s}')
        ## reverse the string as you step through it
        if len(s) == 1:
            return s
        
        ## aa_ -> deque(['a', 'a'])
        ## ...
        ## aabdsd_ -> deque(['d', 's', 'd', 'b' ,'a', 'a'])
        

        ## Initialize
        mirroredString = deque(list(s[1::-1]))
        if s[1] == s[0]:
            # Set the Index 
            longestLength = 2
        else:
            longestLength = 1   ## First Longest String is First Character

    
        palendromeIndex = 1
        longestPaledromeString = s[:longestLength]
        print(f'Start with mirroredString{mirroredString} and looking at position {palendromeIndex}')

        ## Loop along the string
        past = ''
        for index, c in enumerate(s[2:]):
            
            past += c
            while palendromeIndex > -1:
                print(f'ON: {c}, checking position {palendromeIndex} in mirroredString{mirroredString}')
                if c == mirroredString[palendromeIndex]:
                    ## The palendrome grew from length n to n + 1
                    print(f'NEW PALENDOME: {c}, at position {palendromeIndex} in mirroredString{mirroredString}')
                    
                    currentLength = palendromeIndex + 2
                    if palendromeIndex < len(mirroredString) - 1:
                        pass
                        ##palendromeIndex += 1
                    else:
                        ## Have to move the pointer when I get an overflow!
                        palendromeIndex = 0  ## Only symmetrical alternative
                    ##mirroredString.appendleft(c)
                    ## Lets compute the longest Palendrome Here
                    if currentLength > longestLength:
                        longestLength = currentLength
                        print(f'NEW LONGEST with: {c} mirroredString{mirroredString}')
                        longestPaledromeString = c + "".join(list(mirroredString)[:longestLength - 1])                      
                    
                    break
                
                ## There is no palendrome at this charater move left and try again
                palendromeIndex -= 1

            
            
            ## An inserted char is a palendrome all by itself
            mirroredString.appendleft(c)  
            palendromeIndex += 2

        ## Remember Palindromes can jump from length 1 to length 2
        ## ex: b -> bb
        ## ... or from length 1 to length 3
        ## ex: ab -> aba

        print(f'Longest {longestLength}')
        return longestPaledromeString

    print(longestPalindrome("aa"))
    print(longestPalindrome("ab"))
    print(longestPalindrome("aba"))
    print(longestPalindrome("babad"))
    print(longestPalindrome("cbbd"))
    print(longestPalindrome("cbbc"))
    print(longestPalindrome("cbbbccd"))
    print(longestPalindrome("caba"))

    

        

   


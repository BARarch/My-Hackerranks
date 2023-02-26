"""
This code is for LeetCode 5. Longest Palidromic Substring

"""

def fromCenter (s: str) -> str:
    longestPalindromeString = ""
    if len(s) % 2:
        ## Odd string length: both start on same index
        leftCheckInd = longestPalindromeLeft = len(s) // 2
        rightCheckInd = longestPalindromeRight = len(s) // 2

    else:
        ## Even string length: there are two middle characters in the middle
        '''len(s) = 6 inds[0, 1, 2 <- , -> 3, 4, 5]
        we want the 2 and the 3
        3 = len(S) // 2
        2 = (len(S) // 2) - 1
        '''
        leftCheckInd = longestPalindromeLeft = longestPalindromeRight    = (len(s) // 2) - 1
        rightCheckInd =len(s) // 2

    while s[leftCheckInd] == s[rightCheckInd]:
        longestPalindromeLeft, longestPalindromeRight = leftCheckInd, rightCheckInd
        leftCheckInd -= 1
        rightCheckInd += 1

        if leftCheckInd == -1:
            ## The full string is a Palendrome
            res =  s
            #print(f'Center Palendrome for {s}:{res}')
            return res

    
    res =  s[longestPalindromeLeft:longestPalindromeRight + 1]
    #print(f'Center Palendrome for {s}:{res}')
    return res


class Solution:
    def longestPalindrome(self, s: str) -> str:
        print(f"------------------------ s:{s}   -------------------------")
        def longestPalindromeRec(s, longest):   
            if len(longest) > len(s):
                return longest

            if len(s) == 1:
                return s

            centeredPalindrome = fromCenter(s)

            if len(centeredPalindrome) > len(longest):
                longest = centeredPalindrome

            ## Keep Going
            res =  [longest, 
                    longestPalindromeRec(s[:len(s) - 1], longest),
                    longestPalindromeRec(s[1:], longest)]

            res.sort(key=(lambda palendrome: len(palendrome)), reverse=True)
            return res[0]

        res = longestPalindromeRec(s, "")
        print(res)
        return res

# Tester
def test_solution():
    solution = Solution()
    assert solution.longestPalindrome("bbcbd") == "bcb"      # <-- LP at the begining of string
    assert solution.longestPalindrome("cbbc") == "cbbc"     # <-- LP is the full string
    assert solution.longestPalindrome("babad") in ["bab", "aba"]    # <-- DIFFERENT
    assert solution.longestPalindrome("cada") == "ada"      # <-- End of String
    assert solution.longestPalindrome("cabaf") == "aba"      # <-- MIDDLE of String
    assert solution.longestPalindrome("ac") == "a"
    # Add more test cases here

if __name__ == "__main__":

    test_solution()
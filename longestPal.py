"""
This code is for LeetCode 5. Longest Palidromic Substring

"""

def fromCenterFast (s: str) -> str:
    pass

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
    print(f'Center Palendrome for {s}:{res}')
    return res



def getPalentromeAtLoc(s, center, width):
    p = s[center - width: center + width + 1]
    palendrome = ''
    for i in range(1, len(p), 2):
        palendrome += p[i]
    print(p)
    print(palendrome)
    return palendrome


class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Manchesters Algorithm
        originalS = s
        s = "@" + s + "$"
        # s = "caba" -> "@caba$" -> "@#c#a#b#a#$"
        t = ''
        for c in s:
            t += c + '#'
        s = t[:-1]
        # -> "@#c#a#b#a#$"

        p = [0] * len(s)
        longest = 0
        longestLoc = 1
        print(f"------------------------ s:{originalS}   -------------------------")
        for i in range(1, len(s) - 1):
            w = 0
            while s[i - w] == s[i + w]:
                p[i] = w
                w += 1
            if w > longest:
                longest = w
                longestLoc = i

        print(p)
        return getPalentromeAtLoc(s, longestLoc, longest - 1)


    def longestPalindromeMemoize(self, s: str) -> str:
        from collections import deque
        longest = fromCenter(s) #<-- Initialize
        if len(longest) >= len(s) - 1:
            print(f'LONGEST IS {longest}')
            return longest

        viablePalendromes = deque([s[:len(s) - 1], s[1:]])
        
        while viablePalendromes:
            c = viablePalendromes.popleft()
            if len(c) < len(longest):
                ## Terminal Condition
                print(f'LONGEST IS {longest}')
                return longest
            centerPalendrome = fromCenter(c)

            if len(centerPalendrome) > len(longest):
                longest = centerPalendrome


            viable = c[:len(c) - 1]
            if viable != viablePalendromes[-1]:
                viablePalendromes.append(viable)
                
            viablePalendromes.append(c[1:])






    def longestPalindromeSLOW(self, s: str) -> str:
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
    
    assert solution.longestPalindrome("ac") == "a"
    
    assert solution.longestPalindrome("babad") in ["bab", "aba"]    # <-- DIFFERENT
    assert solution.longestPalindrome("caba") == "aba"
    assert solution.longestPalindrome("cabaf") == "aba"      # <-- MIDDLE of String
    
    assert solution.longestPalindrome("cbbc") == "cbbc"     # <-- LP is the full string
    assert solution.longestPalindrome("abb") == "bb"

    assert solution.longestPalindrome("abbcccbbbcaaccbababcbcabca") in ['bbcccbb', 'cbababc']
    assert solution.longestPalindrome("babaddtattarrattatddetartrateedredividerb")

    assert solution.longestPalindrome("reifadyqgztixemwswtccodfnchcovrmiooffbbijkecuvlvukecutasfxqcqygltrogrdxlrslbnzktlanycgtniprjlospzhhgdrqcwlukbpsrumxguskubokxcmswjnssbkutdhppsdckuckcbwbxpmcmdicfjxaanoxndlfpqwneytatcbyjmimyawevmgirunvmdvxwdjbiqszwhfhjmrpexfwrbzkipxfowcbqjckaotmmgkrbjvhihgwuszdrdiijkgjoljjdubcbowvxslctleblfmdzmvdkqdxtiylabrwaccikkpnpsgcotxoggdydqnuogmxttcycjorzrtwtcchxrbbknfmxnonbhgbjjypqhbftceduxgrnaswtbytrhuiqnxkivevhprcvhggugrmmxolvfzwadlnzdwbtqbaveoongezoymdrhywxcxvggsewsxckucmncbrljskgsgtehortuvbtrsfisyewchxlmxqccoplhlzwutoqoctgfnrzhqctxaqacmirrqdwsbdpqttmyrmxxawgtjzqjgffqwlxqxwxrkgtzqkgdulbxmfcvxcwoswystiyittdjaqvaijwscqobqlhskhvoktksvmguzfankdigqlegrxxqpoitdtykfltohnzrcgmlnhddcfmawiriiiblwrttveedkxzzagdzpwvriuctvtrvdpqzcdnrkgcnpwjlraaaaskgguxzljktqvzzmruqqslutiipladbcxdwxhmvevsjrdkhdpxcyjkidkoznuagshnvccnkyeflpyjzlcbmhbytxnfzcrnmkyknbmtzwtaceajmnuyjblmdlbjdjxctvqcoqkbaszvrqvjgzdqpvmucerumskjrwhywjkwgligkectzboqbanrsvynxscpxqxtqhthdytfvhzjdcxgckvgfbldsfzxqdozxicrwqyprgnadfxsionkzzegmeynye")



    '''
    assert fromCenter("cbbc") == 'cbbc'
    assert fromCenter("cbbd") == 'bb'
    assert fromCenter("bz") in ['b', 'z']
    assert fromCenter("adz") == "d"'''

'''
    assert solution.longestPalindrome("babaddtattarrattatddetartrateedredividerb")
    
    assert solution.longestPalindrome("bbcbd") == "bcb"      # <-- LP at the begining of string
    assert solution.longestPalindrome("cbbc") == "cbbc"     # <-- LP is the full string
    
    assert solution.longestPalindrome("cada") == "ada"      # <-- End of String
    assert solution.longestPalindrome("cabaf") == "aba"      # <-- MIDDLE of String
    
    

    assert solution.longestPalindrome("reifadyqgztixemwswtccodfnchcovrmiooffbbijkecuvlvukecutasfxqcqygltrogrdxlrslbnzktlanycgtniprjlospzhhgdrqcwlukbpsrumxguskubokxcmswjnssbkutdhppsdckuckcbwbxpmcmdicfjxaanoxndlfpqwneytatcbyjmimyawevmgirunvmdvxwdjbiqszwhfhjmrpexfwrbzkipxfowcbqjckaotmmgkrbjvhihgwuszdrdiijkgjoljjdubcbowvxslctleblfmdzmvdkqdxtiylabrwaccikkpnpsgcotxoggdydqnuogmxttcycjorzrtwtcchxrbbknfmxnonbhgbjjypqhbftceduxgrnaswtbytrhuiqnxkivevhprcvhggugrmmxolvfzwadlnzdwbtqbaveoongezoymdrhywxcxvggsewsxckucmncbrljskgsgtehortuvbtrsfisyewchxlmxqccoplhlzwutoqoctgfnrzhqctxaqacmirrqdwsbdpqttmyrmxxawgtjzqjgffqwlxqxwxrkgtzqkgdulbxmfcvxcwoswystiyittdjaqvaijwscqobqlhskhvoktksvmguzfankdigqlegrxxqpoitdtykfltohnzrcgmlnhddcfmawiriiiblwrttveedkxzzagdzpwvriuctvtrvdpqzcdnrkgcnpwjlraaaaskgguxzljktqvzzmruqqslutiipladbcxdwxhmvevsjrdkhdpxcyjkidkoznuagshnvccnkyeflpyjzlcbmhbytxnfzcrnmkyknbmtzwtaceajmnuyjblmdlbjdjxctvqcoqkbaszvrqvjgzdqpvmucerumskjrwhywjkwgligkectzboqbanrsvynxscpxqxtqhthdytfvhzjdcxgckvgfbldsfzxqdozxicrwqyprgnadfxsionkzzegmeynye")
    '''
    # Add more test cases here

if __name__ == "__main__":

    test_solution()
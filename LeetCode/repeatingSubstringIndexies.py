'''
This code is for LeetCode 3. Longest Substring Without Repeating Characters
'''

import string

if __name__ == "__main__":

    def lengthOfLongestSubstring(s: str) -> int:
        '''
        "a-bcdaghf" -> abcd -> bcdaghf
        "abc-dcwxyz" -> abcd -> dcwxwyz
        '''
        currentStart = 0
        longest = 0
        currentSubstringIndexies = {}
        for currentEnd, c in enumerate(s):
            if c in currentSubstringIndexies:
                if currentSubstringIndexies[c] >= currentStart:
                    currentStart = currentSubstringIndexies[c] + 1

            ## Increment and Compute Longest
            if currentEnd - currentStart + 1 > longest:
                longest = currentEnd - currentStart + 1

            currentSubstringIndexies[c] = currentEnd

        return longest


    print(lengthOfLongestSubstring("abcabcbb"))
    print(lengthOfLongestSubstring("bbbbb"))
    print(lengthOfLongestSubstring("pwwkew"))

        

   


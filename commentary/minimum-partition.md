# Intuition
k can be compared to any substring that is the same length.  If k is too small, it can be compared to that same substring minus the least signigicant digit, and it will not be too small.  
For example k = 550, is less than 625 but not less than 62. For this problem, optimal substrings are either the same length as k or one digit shorter.
# Approach
Start by comparing k to the first full substring in s, where the first full substring is the left most substring that is the same length as k.  If k is less than that substring, the full substring is the largest substring that could be produced at this step.  There is no better outcome.  In this case, remove that full substring from s and iterate.  If k is smaller than the full substring, another substring is produced at this step, but it isn't the full substring.  Instead, it is the full substring minus the least signigicant digit.  Again, in this case, remove the substring and iterate.  Since each step produces an optimal substring, just count the steps until there are no more digits. 


# Complexity
- Time complexity:
$$O(n)$$ linear in length of string

- Space complexity:
$$O(1)$$ there is no growth.  A sigle string is used and made smaller with every step

# Code
```
class Solution:
    def minimumPartition(self, s: str, k: int) -> int:
        res = 0
        while s:
            res += 1
            if int(s[:len(str(k))]) <= k:
                ##print(f"Move all {int(s[:len(str(k))])} less than {k}")
                s = s[len(str(k)):]
                
            else:
                ##print(f"Move all but one {int(s[:len(str(k))])} greater than {k}")
                if len(str(k)) == 1:
                    return -1
                s = s[len(str(k)) - 1:]
                
        return res
                
                
     
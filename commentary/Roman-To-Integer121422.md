# Intuition
Here we match patterns in the roman numeral to tally up the integer value.

# Approach
There are two dicts. *Solids* with "I, V, X, ..., M" as keys and "1, 5, 10, ..., 1000" as values. Then *oneless* with "IV, IX, XL, ..., CM" as keys and "4, 9, 40, ..., 900" as values.  We revmove from the string the keys of the *oneless* dict if they are present and talley the values accordingly.  The loop through an increment the talley by the corresponding values in the *solids*

# Complexity
- Time complexity:
$$O(n)$$ What is checked for and removed is fixed. So the size of string n.

- Space complexity:
$$O(n)$$ size of string n.

# Code
```
class Solution:
    def romanToInt(self, s: str) -> int:
        oneLess = { "IV": 4,
                    "IX": 9,
                    "XL": 40,
                    "XC": 90,
                    "CD": 400,
                    "CM": 900
                    }

        solids = {  "I": 1,
                    "V": 5,
                    "X": 10,
                    "L": 50,
                    "C": 100,
                    "D": 500,
                    "M": 1000
                    }

        d = 0
        for symbol in oneLess:
            if symbol in s:
                d += oneLess[symbol]
                s = s.replace(symbol, "")

        for c in s:
            d += solids[c]

        return d


```
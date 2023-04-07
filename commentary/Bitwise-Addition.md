# Intuition
This is my attempt at doing bitwise addition accross a string in golang.  We start at the end of each string. Base 2 addition can be done digit by digit. The proper solution would be achieved this way by capturing the nessary carry additions in the case of overflow.

# Approach
I have a long way to GO on this one(what a pun)!  The big take away is that this a solution without strconv.  Although I later found that strconv is availible, this solution was coded without the knowlege of the package in this context.  To execute the additions, a series of cumbersome conversions needed to be carried out.  The rune values at each character were converted to boolean values.  The boolean values were run through logical expressions to produce the result and carry bits for every digit of the addition.  The result was a slice of boolean values, representing the sequence of bits of the solution.  The slice of booleans was again converted back to a string. Whoa!

# Complexity
- Time complexity:
$$O(n)$$ linear in the length of the longest digit string

- Space complexity:
$$O(n)$$ linear in the lenght of both strings

# Code
```
func addBinary(a string, b string) string {
    r := make([]bool, 0)
    carry := false

    var longest, shortest string
    if len(a) > len(b) {
        longest = a
        shortest = b
    } else {
        longest = b
        shortest = a
    }

    var i, j int
    var aa, bb bool
    for t := range longest {
        // Indexies: loop backwards
        i = len(longest) - 1 - t
        j = len(shortest) - 1 - t

        // Values: byte values 48 and 49 represent our binary 0s and 1s respectively in our case
        // check to see if we've run out of values in the shorter number string
        aa = asc2Bool(longest[i])
        if j < 0 {
            // Run out of digits in the shorter number
            bb = false
        } else {
            bb = asc2Bool(shortest[j])
        }

        r = append(r, resultSum(aa, bb, carry)) // Bitwise Addition Logic
        carry = carrySum(aa, bb, carry)       // Carry Flag
    }
    // Add Last 1 if there is a carry after last addition
    if carry {
        r = append(r, true)
    }
    return bool2str(r)
}

func resultSum(a bool, b bool, c bool) bool {
	return a != b != c
}

func carrySum(a bool, b bool, c bool) bool {
	return (a && b) || (a && c) || (b && c)
}

func asc2Bool(val byte) bool {
	if val == 48 {
		return false
	}
	if val == 49 {
		return true
	}
	return false
}

func bool2str(vals []bool) string {
	var res string = ""
	for i := range vals {
		i = len(vals) - 1 - i
		if vals[i] {
			res += "1"
		} else {
			res += "0"
		}
	}
	return res
}
```
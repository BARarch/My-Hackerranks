# Intuition
A number represented as a mirored slice is incremented.  A single digit is one element.  Carry and overflow conditions from cases where a 9 is incremented require iteration.  These cases produce a [1, 0] instead of just a [10], and trigger the next sigigicant digit to be incrememnted.

# Approach
This is a deep dive into slice opperations.  There are better approaches. I did this exercise to learn slice manipulation.  

Start by incrmenting the last digit.  If it is a 9 that carries when incremented, the carry flag is set and we iterate to increment the next digit.  This contintues until there's an incrementation without a carry.  If there is a carry resulting from incrementing the most significant digit, a 1 is appended to the end of the solution and we stop.

Mathematically this process works from the least signigicant to the most significant digit, or right to left.  For simplicity, the solution slice is appended left to right when computed.  The solution has to be reversed to be correct.

# Complexity
- Time complexity:
$$O(n)$$ linear in worst case if every digit is a 9.

- Space complexity:
$$O(n)$$ linear in the number of digits

# Code
```
func plusOne(digits []int) []int {

    // from [...,9]
    // to   [...,1, 0]
    // so check len(digits - 3) onward nope! -> Easier to reverse slice -> Do math -> reverse again
    r := reverse(digits)

    for carry, pos := true, 0 ; carry ; pos++ {
        if pos == len(r) {
            r = append(r, 1)
            carry = false
        } else {
            if r[pos] == 9 {
                r[pos] = 0
                carry = true
            } else {
                r[pos]++
                carry = false
            }
        }
        
    }
     
    return reverse(r)
}

func reverse(s []int) []int {
    for i, j := 0, len(s) - 1; i < j; i, j = i + 1, j - 1{
        s[i], s[j] = s[j], s[i]
    }
    return s
}
```
"""
This code is for LeetCode X

"""



class Solution:
    def convert(self, s: str, numRows: int) -> str:
        N = numRows - 1  
        rows = ["" for i in range(numRows)]
        for i, c in enumerate(s):
            if (i // N) % 2 == 0:
                rows[i % N] += c
            else:
                rows[N - (i % N)] += c

        return ''.join(rows)




# Tester
def test_solution():
    solution = Solution()
    assert solution.convert("PAYPALISHIRING", 3) == "PAHNAPLSIIGYIR"
    assert solution.convert("PAYPALISHIRING", 4) == "PINALSIGYAHRPI"


if __name__ == "__main__":

    test_solution()
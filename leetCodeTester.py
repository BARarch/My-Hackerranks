class Solution:
    def twoSum(self, nums, target):
        # implementation here
        return [0, 1]

# Tester
def test_solution():
    solution = Solution()
    assert solution.twoSum([2, 7, 11, 15], 9) == [0, 1]
    assert solution.twoSum([3, 2, 4], 6) == [1, 2]
    assert solution.twoSum([3, 3], 6) == [0, 1]
    # Add more test cases here

if __name__ == "__main__":

    test_solution()
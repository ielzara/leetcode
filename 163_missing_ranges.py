from typing import List


class Solution:
    def findMissingRanges(
        self, nums: List[int], lower: int, upper: int
    ) -> List[List[int]]:
        result = []

        # Function to add range to the result
        def add_range(start, end):
            if start <= end:
                result.append([start, end])

        # Handle the lower boundary
        next_num = lower
        for num in nums:
            if num > next_num:
                add_range(next_num, num - 1)
            next_num = num + 1

        # Handle the upper boundary
        add_range(next_num, upper)

        return result


# Example usage
x = Solution()
print(x.findMissingRanges(nums=[0, 1, 3, 50, 75], lower=0, upper=99))  # Example 1
print(x.findMissingRanges(nums=[-1], lower=-1, upper=-1))  # Example 2

from typing import List


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        # Step 1: Sort the array
        nums.sort()

        # Step 2 and 3: Sum up the first element of each pair
        sum_min = 0
        for i in range(0, len(nums), 2):
            sum_min += nums[i]

        return sum_min

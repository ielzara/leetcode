from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        set_nums = set(nums)
        disappeared = []
        for num in range(1, len(nums) + 1):
            if num not in set_nums:
                disappeared.append(num)

        return disappeared
        
from typing import List

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums_set = set(nums)
        nums_list = list(nums_set)
        nums_list.sort()
        if len(nums_list) < 3:
            return nums_list[-1]
        else:
            return nums_list[-3]
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()

        for i, k in enumerate(nums):
            if i != k:
                return i
        return len(nums)
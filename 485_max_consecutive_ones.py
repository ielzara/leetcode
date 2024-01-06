class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_consecutive = 0
        count = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
                max_consecutive = max(max_consecutive, count)
            else:
                count = 0
            return max_consecutive

from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if not nums:
            return
        count = 0
        candidate = None
        for num in nums:
            if count == 0:
                candidate = num
            if num == candidate:
                count +=1
            else:
                count -=1

        if nums.count(candidate) > len(nums) // 2:
            return candidate
        else:
            return


x = Solution()
print(x.majorityElement([2, 2, 1, 1, 1, 2, 2]))

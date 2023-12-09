from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if not nums:
            return
        majority = {}
        for num in nums:
            if num not in majority:
                majority[num] = 1
            else:
                majority[num] += 1
        largest_key = max(majority, key=majority.get)

        return largest_key


x = Solution()
print(x.majorityElement([2, 2, 1, 1, 1, 2, 2]))

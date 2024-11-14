from typing import List


class Solution:
    def findLHS(self, nums):
        # Step 4: Use a hash table to count elements
        count = {}
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1

        # Step 5 and 6: Iterate and compute the maximum length
        max_length = 0
        for num in count:
            if num + 1 in count:
                max_length = max(max_length, count[num] + count[num + 1])

        return max_length

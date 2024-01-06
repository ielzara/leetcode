from typing import List


class Solution:
    def nextGreaterElement(self, nums1, nums2):
        # Create a dictionary to hold the next greater element for each number in nums2
        next_greater = {}
        stack = []

        # Traverse through nums2 to fill the next_greater dictionary
        for num in nums2:
            while stack and stack[-1] < num:
                next_greater[stack.pop()] = num
            stack.append(num)

        # For elements remaining in the stack, there is no next greater element
        for num in stack:
            next_greater[num] = -1

        # Build the result for nums1 using the next_greater dictionary
        result = []
        for num in nums1:
            result.append(next_greater[num])

        return result


# Example usage
solution = Solution()
nums1 = [4, 1, 2]
nums2 = [1, 3, 4, 2]
print(solution.nextGreaterElement(nums1, nums2))  # Output: [-1, 3, -1]

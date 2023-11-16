class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashTable = {}

        for i, key in enumerate(nums):
            complement = target- key
            if complement in hashTable:
                return [hashTable[complement], i]
            hashTable[key] = i
        return []
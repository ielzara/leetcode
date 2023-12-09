
def removeElement(nums, val) -> int:
    x=0
    while (val in nums):
        if nums[x] == val:
            nums.remove(nums[x])
            x-=1
        x+=1
    print(str(len(nums)) + ", " + str(nums))
    return len(nums)
    
nums = [0,1,2,2,3,0,2,4]
val = 2
k = removeElement(nums, val)
# class Solution:
#     def removeElement(self, nums: List[int], val: int) -> int:
#         count = len(nums)
#         for val in nums:
#             if val in nums:
#                      n nums[val] = '_'
#                 count -= 1
#         if val 



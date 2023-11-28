# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]):
        if not nums:
            return

        mid = len(nums) // 2

        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])  # left subtree
        root.right = self.sortedArrayToBST(nums[mid + 1 :])  # right subtree
        return root

#     def tree_to_list(self, root: TreeNode):
#         lists = []
#         self.tree_to_lists(root, lists, 0)

#         ret = []
#         for l in lists:
#             while l and l[-1] is None:
#                 l.pop()
#             ret += l
#         return ret

#     def tree_to_lists(self, root: TreeNode, lists: List[List[int]], level: int):
#         while len(lists) < level + 1:
#             lists.append([])
#         if not root:
#             lists[level].append(None)
#             return
#         lists[level].append(root.val)
#         self.tree_to_lists(root.left, lists, level + 1)
#         self.tree_to_lists(root.right, lists, level + 1)


# x = Solution()
# root = x.sortedArrayToBST([-10, -3, 0, 5, 9])

# print(x.tree_to_list(root))

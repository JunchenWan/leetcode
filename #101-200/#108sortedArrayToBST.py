# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """

        if not nums:
            return None

        index = len(nums) // 2
        root = TreeNode(nums[index])
        left = nums[:index]
        right = nums[index + 1:]
        root.left = self.sortedArrayToBST(left)
        root.right = self.sortedArrayToBST(right)

        return root
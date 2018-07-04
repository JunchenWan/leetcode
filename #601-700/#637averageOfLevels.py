# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """

        stack = [root]
        ans = []
        while stack:
            tmp = 0
            total = len(stack)
            for i in range(0, total):
                current = stack.pop(0)
                tmp = tmp + current.val
                if current.left:
                    stack.append(current.left)
                if current.right:
                    stack.append(current.right)
            ans.append(tmp / (total / 1.0))
        return ans
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root.left == None and root.right == None: return 0

        stack = []
        lists = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            if stack:
                tmp = stack.pop()
                lists.append(tmp.val)
                root = tmp.right
        ans = float('Inf')
        for i in range(0, len(lists) - 1):
            ans = min(ans, abs(lists[i] - lists[i + 1]))

        return ans
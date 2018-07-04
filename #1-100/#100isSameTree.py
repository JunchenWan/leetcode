# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p == None and q == None:
            return True
        if p == None or q == None:
            return False

        stackp = [p]
        stackq = [q]

        while stackp and stackq:
            currentp = stackp.pop(0)
            currentq = stackq.pop(0)
            if currentp.val != currentq.val:
                return False
            if currentp.left and currentq.left:
                stackp.append(currentp.left)
                stackq.append(currentq.left)
            else:
                if currentp.left or currentq.left:
                    return False
            if currentp.right and currentq.right:
                stackp.append(currentp.right)
                stackq.append(currentq.right)
            else:
                if currentp.right or currentq.right:
                    return False

        return True

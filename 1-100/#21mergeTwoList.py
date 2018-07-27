# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l2 == None: return l1
        if l1 == None: return l2

        if l1.val > l2.val:
            r1 = l2
            l2 = l2.next
        else:
            r1 = l1
            l1 = l1.next
        r2 = r1
        while (l1 != None) or (l2 != None):
            if l1 == None:
                r1.next = l2
                return r2
            if l2 == None:
                r1.next = l1
                return r2
            if l1.val > l2.val:
                r1.next = l2
                l2 = l2.next
                r1 = r1.next
            else:
                r1.next = l1
                l1 = l1.next
                r1 = r1.next
        return r2


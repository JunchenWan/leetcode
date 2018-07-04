# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if head == None or head.next == None:
            return head
        lis = head
        while lis:
            if lis.next and lis.next.val == lis.val:
                lis.next = lis.next.next
            else:
                lis = lis.next
        return head
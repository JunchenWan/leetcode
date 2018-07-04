# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None or head.next == None:
            return False
        else:
            fast = head.next
            slow = head
            while fast != None:
                if fast == slow:
                    return True
                else:
                    fast = fast.next
                    if fast == None:
                        return False
                    else:
                        fast = fast.next
                        slow = slow.next

            return False

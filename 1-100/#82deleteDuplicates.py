class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head


        lis = head
        newhead = ListNode(0)
        tmp = newhead
        while lis:
            if lis.next and lis.next.val ==lis.val:
                while lis.next and lis.next.val == lis.val:
                    lis = lis.next
            else:
                tmp.next = lis
                tmp = tmp.next
            lis = lis.next

        tmp.next = lis
        return newhead.next

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

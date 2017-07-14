# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        length = self.getLen(head)
        p = head
        if length == n:
            head = head.next
            return head
        for _ in range(length - n -1):
            p = p.next
        p.next = p.next.next
        return head
        
    def getLen(self, head):
        p = head
        length = 0
        while p != None:
            length += 1
            p = p.next
        return length

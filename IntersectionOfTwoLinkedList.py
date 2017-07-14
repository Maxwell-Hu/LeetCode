# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        lenA = self.get_len(headA)
        lenB = self.get_len(headB)
        pA = headA
        pB = headB
        if lenA > lenB :
            pA = self.move_pointer(pA, lenA-lenB)
        elif lenA < lenB:
            pB = self.move_pointer(pB, lenB-lenA)
        for i in range(min(lenA,lenB)):
            if pA.val == pB.val:
                break
            pA = pA.next
            pB = pB.next
        if pA == pB :
            return pA
        else:
            return
        
    def get_len(self, head):
        len = 0
        while head != None:
            len += 1
            head = head.next
        return len
    
    def move_pointer(self,head, length):
        for _ in range(length):
            head = head.next
        return head

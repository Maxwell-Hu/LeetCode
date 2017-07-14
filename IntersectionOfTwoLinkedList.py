# Definition for singly-linked list.
#class ListNode(object):
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        listA = self.traversal(headA)
        listB = self.traversal(headB)
        listA.reverse()
        listB.reverse()
        p = 0
        for i in range(min(len(listA),len(listB))):
            p = i
            if listA[i] != listB[i] or listA[i][0] == None:
                break
        if p == 0 :
            return
        else :
            return listA[p][1]
    
    def traversal(self,head):
        listP = [[None,head]]
        while head != None :
            tmpP = [head.val,head.next]
            listP.append(tmpP)
            head = head.next
        return listP

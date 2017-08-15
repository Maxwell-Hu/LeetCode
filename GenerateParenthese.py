class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.result = []
        left, right = n,n
        strings = ''
        self.helper(left,right,strings)
        return self.result
        
    def helper(self,left, right, strings):
        if left == right and left == 0:
            self.result.append(strings)
            return
        if left == right: self.helper(left-1,right,strings + '(')
        elif left == 0: self.helper(left,right-1,strings + ')')
        else:
            self.helper(left-1,right,strings+'(')
            self.helper(left,right-1,strings+')')

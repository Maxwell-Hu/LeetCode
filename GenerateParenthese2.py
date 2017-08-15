class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def generate(p, left, right, paren=[]):
            if left: generate(p+'(', left-1, right)
            if right > left: generate(p+')', left, right-1)
            if not right: paren += p,
            return paren
        return generate('',n,n)

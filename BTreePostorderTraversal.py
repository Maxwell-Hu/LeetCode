# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = [root]
        ret = []
        while stack:
            node = stack.pop()
            if node:
                ret.append(node.val)
                stack.append(node.left)
                stack.append(node.right)
        ret.reverse()
        return ret

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.result = []
        
    def preorder(self, root):
        if root != None:
            self.result.append(root.val)
            self.preorder(root.left)
            self.preorder(root.right)
    
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.preorder(root)
        return self.result

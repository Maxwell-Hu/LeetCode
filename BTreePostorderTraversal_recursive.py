# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.valList = []
        
    def recursiveTraversal(self, root):
        if root == None : return
        if self.recursiveTraversal(root.left) != None: self.valList.append(self.recursiveTraversal(root.left)) 
        if self.recursiveTraversal(root.right) != None: self.valList.append(self.recursiveTraversal(root.right)) 
        self.valList.append(root.val)
        
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.recursiveTraversal(root)
        return self.valList

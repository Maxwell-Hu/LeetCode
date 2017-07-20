# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if preorder:
            node = TreeNode(preorder[0])
            idx = inorder.index(preorder[0])
            node.left = self.buildTree(preorder[1:1+idx],inorder[:idx])
            node.right = self.buildTree(preorder[1+idx:],inorder[idx+1:])
            return node
        else:
            return None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    def invertHelper(self, root):
        if (root == NULL):
            return root
        
        temp = root.left
        root.left = invertHelper(root.right)
        root.right = invertHelper(temp)
        
        
        return root
        
    
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        return invertHelper(root)
        

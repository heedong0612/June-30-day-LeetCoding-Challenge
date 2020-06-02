class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invertTree(self, root: TreeNode) -> TreeNode:
    '''
    invert tree
    '''
    def helper(node: TreeNode):
        '''
        Recursive helper method
        switch children's children then switch children 
        '''
        if node == None: 
            return
        
        helper(node.left)
        helper(node.right)
        
        temp = node.left
        node.left = node.right
        node.right = temp
    
    helper(root)
    return root
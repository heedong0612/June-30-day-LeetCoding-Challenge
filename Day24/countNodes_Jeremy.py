class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def countNodes(root: TreeNode) -> int:
    # base case
    if not root:
        return 0
    
    # recursive case
    return 1 + countNodes(root.left) + countNodes(root.right)
    
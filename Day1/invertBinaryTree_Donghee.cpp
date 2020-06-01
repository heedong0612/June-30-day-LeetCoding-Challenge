// 6/1/2020
// Donghee Lee

class Solution {
public:
    TreeNode* invertTree(TreeNode* root) {
        return invertHelper(root);
    }
    
    TreeNode* invertHelper(TreeNode* root) {
        if (root == nullptr) return nullptr;
        
        TreeNode* temp = root->left;
        root->left = invertHelper(root->right);
        root->right = invertHelper(temp);
        
        return root;
    }
};
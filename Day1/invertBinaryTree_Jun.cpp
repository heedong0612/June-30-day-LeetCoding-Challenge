// 6/1/2020

class Solution {
public:
    TreeNode* invertTree(TreeNode* root) {
        if (root == NULL) {
            return NULL;
        }
        queue<TreeNode*> que; 
        que.push(root);
        while (!que.empty()) {
            TreeNode* current = que.front();
            TreeNode* temp = current->left;
            current->left = current->right;
            current->right = temp;
            if (current->left != NULL) {
                que.push(current->left);
            }
            if (current->right != NULL) {
                que.push(current->right);
            }
            que.pop();
        }
        return root;
    }
};
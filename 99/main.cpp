/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
private:
    TreeNode* leftAdjc(TreeNode* root){
        TreeNode* node = root->left;
        while (node!=nullptr && node->right!=nullptr){
            if (node->right == root){
                return node;
            }
            node = node->right;
        }
        return node;
    }
    void _recoverTree(TreeNode* node, TreeNode* preRight, TreeNode *& big, TreeNode *& small){
        if (node == nullptr) 
            return;
        
        auto lf = leftAdjc(node);
        if (lf == nullptr || lf->right == node) {
            // visit this node
            if (lf != nullptr)
                lf->right = nullptr;
            else{
                lf = preRight;
            }
            if (lf != nullptr){
                if (lf->val > node->val){
                    small = node;
                    if (big == nullptr)
                        big = lf;
                }
            }

            // travel right
            return _recoverTree(node->right, node, big, small);
        }
        // travel left
        lf->right = node;
        return _recoverTree(node->left, preRight, big, small);
    }
public:
    void recoverTree(TreeNode* root) {
        TreeNode* big = 0, *small = 0;
        _recoverTree(root, nullptr, big, small);
        swap(big->val, small->val);
    }
};
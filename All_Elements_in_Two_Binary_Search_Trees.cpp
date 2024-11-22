/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    vector<int>ans;
    void inorder(TreeNode * root){
        if(root == NULL){
            return ;
        }
        inorder(root->left);
        ans.push_back(root->val);
        inorder(root->right);

    }
    vector<int> getAllElements(TreeNode* root1, TreeNode* root2) {

        inorder(root1);
        inorder(root2);
        int n = ans.size();
        for(int i = 0;i<n;i++){
            for(int j = i+1;j<n;j++){
                if(ans[i]>ans[j]){
                    int temp = ans[i];
                    ans[i] = ans[j];
                    ans[j] = temp;
                }
            }
        }
        return ans;
        
    }
};

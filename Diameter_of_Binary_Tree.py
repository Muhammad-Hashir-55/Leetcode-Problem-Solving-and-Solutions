# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxi = [0]
        def dfs(node):
            if(not node):
                return 0
            
            left_m = dfs(node.left)
            right_m = dfs(node.right)

            maxi[0] = max(maxi[0],left_m + right_m)

            return 1 + max(left_m, right_m)
        
        dfs(root)
        return maxi[0]
        

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        def dfs(root,curr):
            if(not root):
                return False
            curr += root.val
            if(root.left is None and root.right is None):
                if(curr == targetSum):
                    return True
            return dfs(root.left,curr) or dfs(root.right,curr)



        return dfs(root,0)

        

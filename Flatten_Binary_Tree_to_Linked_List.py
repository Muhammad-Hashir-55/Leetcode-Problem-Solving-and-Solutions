# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        arr = []
        def dfs(root):
            if(root == None):
                return
            arr.append(root.val)
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        temp = root
        prev = None
        for i in arr:
            if(temp == None):
                temp = TreeNode(i)
                prev.right = temp
                prev = temp
                temp = temp.right
            else:
                temp.left = None
                temp.val = i
                prev = temp
                temp = temp.right
        
            
        return root

        

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        arr = []
        s = ''
        
        def dfs(root,s):
            if(not root):
                return 
            
            s += str(root.val)
            if(root.left == None and root.right == None):
                arr.append(int(s))
                return 
            
            dfs(root.left,s)
            dfs(root.right,s)
        dfs(root,s)
        print(arr)
        return sum(arr)
        
        

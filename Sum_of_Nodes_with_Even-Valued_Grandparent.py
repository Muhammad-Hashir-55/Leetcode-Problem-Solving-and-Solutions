# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        arr = []
        def dfs(root):
            if(root == None):
                return
            if(root.val % 2 == 0):
                if(root.left):
                    if(root.left.left):
                        arr.append(root.left.left.val)
                    if(root.left.right):
                        arr.append(root.left.right.val)
                if(root.right):
                    if(root.right.left):
                        arr.append(root.right.left.val)
                    if(root.right.right):
                        arr.append(root.right.right.val)
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return sum(arr)
        

        

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: TreeNode | None) -> int:
        arr = []

        def dfs(node,s):
            if(not node):
                return
            
            s += str(node.val)
            if(not node.left and not node.right):
                arr.append(s)
                return

            dfs(node.left,s)
            dfs(node.right,s)
        dfs(root,'')

        tot = 0
        n = len(arr)
        for i in range(n):
            tot += int(arr[i],2)

        return tot



        

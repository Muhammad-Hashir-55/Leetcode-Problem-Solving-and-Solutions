# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def dfs(arr):
            if(len(arr)==0):
                return
            maxi = max(arr)
            idx = arr.index(maxi)
            root = TreeNode()
            root.val = maxi
            root.left = dfs(arr[:idx])
            root.right = dfs(arr[idx +1:])
            return root
        return dfs(nums)
        

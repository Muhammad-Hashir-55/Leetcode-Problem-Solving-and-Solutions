# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__ (self):
        self.arr = []
    def ino(self,root):
        if(root == None):
            return 
        self.ino(root.left)
        self.arr.append(root.val)
        self.ino(root.right)

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.ino(root)

        return self.arr[k-1]

        

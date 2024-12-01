# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.arr = []
    def pos(self,root):
        if(root == None):
            return 
        self.pos(root.left)
        self.pos(root.right)
        self.arr.append(root.val)
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.pos(root)
        return self.arr
        

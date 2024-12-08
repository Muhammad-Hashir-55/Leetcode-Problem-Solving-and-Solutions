# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.arr =[]
    def inn(self,root):
        if(root == None):
            return 
        self.inn(root.left)
        self.arr.append(root.val)
        self.inn(root.right)

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.inn(root)
        return self.arr
        
        

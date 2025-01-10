# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insert(self,root,x):
        if(root== None):
            temp = TreeNode(x)
            return temp
        if(x<root.val):
            root.left = self.insert(root.left,x)
        elif(x>root.val):
            root.right =self.insert(root.right,x)
        return root

            

    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        root = None
        for i in preorder:
            root =self.insert(root,i)
        return root
        

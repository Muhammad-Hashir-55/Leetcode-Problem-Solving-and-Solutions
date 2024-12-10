# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.arr = []
    def pre(self,root):
        if(root == None):
            return
        self.arr.append(root.val)
        self.pre(root.left)
        self.pre(root.right)


    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        self.pre(root)
        x = []
        x = self.arr
        x = set(x)
        l = []
        for i in x:
            l.append(i)
        l.sort()
        if(len(l)==1):
            return -1
        else:
            return l[1]
        

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.arr= []
    def ino(self ,root):
        if(root == None):
            return
        self.ino(root.left)
        self.arr.append(root.val)
        self.ino(root.right)



    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.ino(root)
        if(not self.arr):
            return 0
        n = len(self.arr)
        if(n ==1):
            return 0
        mini = 999999999
        for i in range(n-1):
            if(mini > abs(self.arr[i] - self.arr[i+1])):
                mini = abs(self.arr[i] - self.arr[i+1])
        return mini
        

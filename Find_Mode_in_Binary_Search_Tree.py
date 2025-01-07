# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.dic = {}
    def ino(self,root):
        if(root == None):
            return
        self.ino(self.ino(root.left))
        if(root.val in self.dic):
            self.dic[root.val] +=1
        else:
            self.dic[root.val] =1
        self.ino(self.ino(root.right))
        
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        self.ino(root)
        maxi = max(self.dic.values())
        arr = []
        for i in self.dic:
            if(self.dic[i]== maxi):
                arr.append(i)
        return arr
        

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        arr= []
        def ino(root):
            if(root == None):
                return
            ino(root.left)
            arr.append(root.val)
            ino(root.right)
        ino(root)
        dic = {}
        idx = 0
        for i in arr:
            dic[i] = (sum(arr[idx:]))
            idx +=1
        
        def nino(root):
            if(not root):
                return
            nino(root.left)
            root.val = dic[root.val]
            nino(root.right)
        nino(root)
        return root

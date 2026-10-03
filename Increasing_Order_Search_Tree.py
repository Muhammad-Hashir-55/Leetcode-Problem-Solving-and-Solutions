# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode | None) -> TreeNode | None:

        arr = []

        def ino(root):
            if(not root):
                return
            
            ino(root.left)
            arr.append(root.val)
            ino(root.right)
        ino(root)
        root = TreeNode(arr[0])
        nex = root
        for i in arr[1:]:
            node = TreeNode(i)
            nex.right = node
            nex = nex.right
        return root

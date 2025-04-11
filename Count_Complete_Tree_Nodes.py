# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        q = [root]
        arr = []
        if(not root):
            return 0
        while(q):
            for i in range(len(q)):
                node = q.pop(0)
                arr.append(node.val)
                if(node.left):
                    q.append(node.left)
                if(node.right):
                    q.append(node.right)
        return len(arr)
        

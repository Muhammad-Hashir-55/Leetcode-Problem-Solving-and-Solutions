# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        q = [root]
        arr = []
        while(q):
            for i in range(len(q)):
                node = q.pop(0)
                if(node.left):
                    q.append(node.left)
                    if(not node.left.left and not node.left.right):
                        arr.append(node.left.val)
                if(node.right):
                    q.append(node.right)
        return sum(arr)
        

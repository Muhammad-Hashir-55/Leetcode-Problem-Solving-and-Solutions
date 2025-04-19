# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        q = [root]
        bg = []
        while(q):
            x = []
            for i in range(len(q)):
                node = q.pop(0)
                x.append(node.val)
                if(node.left):
                    q.append(node.left)
                if(node.right):
                    q.append(node.right)
            bg.append(x)
        return sum(bg[-1])
        
        

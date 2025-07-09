# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        q = [root]
        depth = 0
        if(not root):
            return 0
        while(q):
            for i in range(len(q)):
                node = q.pop(0)
                if(node.left):
                    q.append(node.left)
                if(node.right):
                    q.append(node.right)
                


            depth +=1
        return depth
        

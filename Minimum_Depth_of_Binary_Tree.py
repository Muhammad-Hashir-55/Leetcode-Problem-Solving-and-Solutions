# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        q = [root]
        depth = 1
        c = False
        if(not root):
            return 0
        while(q):
            for i in range(len(q)):
                node = q.pop(0)
                if(not node.left and not node.right):
                    c = True
                    break
                if(node.left):
                    q.append(node.left)
                if(node.right):
                    q.append(node.right)


            if(c == True):
                    break
            depth +=1
        return depth

        

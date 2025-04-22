# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        lev = 0
        q = [root]
        while(q):
            if(lev % 2 != 0):
                i = 0
                j = len(q) -1
                while(i < j):

                    q[i].val,q[j].val = q[j].val , q[i].val
                    i +=1
                    j -=1
            lev +=1
            for i in range(len(q)):
                node = q.pop(0)
                if(node.left):
                    q.append(node.left)
                if(node.right):
                    q.append(node.right)
        return root
        

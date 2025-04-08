# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        bg = []
        q = [root]
        c = False
        if(not root):
            return []
        while(q):
            x = []
            for i in range(len(q)):
                node = q.pop(0)
                x.append(node.val)
                if(node.left):
                    q.append(node.left)
                if(node.right):
                    q.append(node.right)
            if(c == False):
                bg.append(x)
                c = True
            else:
                bg.append(x[::-1])
                c = False
        return bg

        

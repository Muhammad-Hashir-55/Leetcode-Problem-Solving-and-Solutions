# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        if(root is None):
            return None
        que= [root]

        while(que):
            node = que.pop(0)
            if(node.val > p.val and node.val > q.val):
                if(node.left):
                    que.append(node.left)
            elif(node.val < p.val and node.val < q.val):
                if(node.right):
                    que.append(node.right)
            else:
                return node
        

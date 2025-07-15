# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        dic = {}

        q = [root]
        sumi = 0

        while(q):
            node = q.pop(0)
            sumi += node.val
            if(node.left):
                q.append(node.left)
            if(node.right):
                q.append(node.right)

        arr = []
        arr.append(sumi)
        
        def pos(root):
            if(not root):
                return
            
            pos(root.left)
            dic[root.val] = arr[-1]
            arr[-1] -= root.val
            pos(root.right)
            
            
        
        pos(root)

        q = [root]
        while(q):
            node = q.pop(0)
            node.val = dic[node.val]
            if(node.left):
                q.append(node.left)
            if(node.right):
                q.append(node.right)
        return root

        

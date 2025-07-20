# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        
        def bfs(root):
            q = [root]
            sumi = 0
            n = 0
            while(q):
                node = q.pop(0)
                sumi += node.val
                n +=1
                if(node.left):
                    q.append(node.left)
                if(node.right):
                    q.append(node.right)
        
            return sumi/n

        q = [root]

        coun = 0

        while(q):
            node = q.pop(0)
            storing = node.val
            matching = bfs(node)
            matching = int(matching)

            if(storing == matching):
                coun +=1
            if(node.left):
                q.append(node.left)
            if(node.right):
                q.append(node.right)
        return coun




        

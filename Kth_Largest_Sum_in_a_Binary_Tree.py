# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        q = [root]
        bg = []
        while(q):
            x =[]
            for i in range(len(q)):
                node = q.pop(0)
                x.append(node.val)
                if(node.left):
                    q.append(node.left)
                if(node.right):
                    q.append(node.right)
            bg.append(x)
        
        n = len(bg)
        if(k>n):
            return -1
        arr = []
        for i in bg:
            arr.append(sum(i))
        arr.sort()
        return arr[-k]
        
        

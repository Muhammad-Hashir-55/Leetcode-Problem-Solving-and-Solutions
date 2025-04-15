# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        q = [root]
        eve = True
        while(q):
            x = []
            for i in range(len(q)):
                node = q.pop(0)
                x.append(node.val)
                if(node.left):
                    q.append(node.left)
                if(node.right):
                    q.append(node.right)
            if(eve == True):
                n = len(x)
                if(n ==1):
                    if(x[0] % 2 == 0):
                        return False
                for i in range(n-1):
                    if(x[i]%2 == 0 or x[i+1]%2 == 0 or x[i]>=x[i+1]):
                        return False
                eve = False
            else:
                n = len(x)
                if(n == 1):
                    if(x[0] % 2 != 0):
                        return False
                for i in range(n-1):
                    if(x[i]%2 != 0 or x[i+1]%2 != 0 or x[i]<=x[i+1]):
                        return False
                eve = True
            
            
        return True

                
        

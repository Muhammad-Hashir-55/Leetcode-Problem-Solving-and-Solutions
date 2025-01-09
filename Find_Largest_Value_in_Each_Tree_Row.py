# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# # important================================
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        arr = []
        q= []
        if(root == None):
            return []
        q.append(root)
        
        while(q):
            x = []
            level_size = len(q)
            for i in range(level_size):
                node = q.pop(0)
                x.append(node.val)
            
                if(node.left != None):
                    q.append(node.left)
                if(node.right != None):
                    q.append(node.right)
            arr.append(x)
        
        aa = []
        
        for i in arr:
            aa.append(max(i))
        return aa

        

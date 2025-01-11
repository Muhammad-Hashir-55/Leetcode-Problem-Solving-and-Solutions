# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# noiceeee
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        arr = []
        q = []
        q.append(root)
        if(not root):
            return []
        while(q):
            x =[]
            leng = len(q)
            for i in range(leng):
                node = q.pop(0)
                x.append(node.val)
                if(node.left != None):
                    q.append(node.left)
                if(node.right != None):
                    q.append(node.right)
            arr.append(x)
        return arr[::-1]

        

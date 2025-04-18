# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        arr = []
        q = [root]
        while(q):
            for i in range(len(q)):
                node = q.pop(0)
                if(node.val >=low and node.val <=high):
                    arr.append(node.val)
                if(node.left):
                    q.append(node.left)
                if(node.right):
                    q.append(node.right)
        root = None
        
        def insert(root,x):
            if(root == None):
                temp = TreeNode(x)
                return temp
            if(x < root.val):
                root.left = insert(root.left,x)
            else:
                root.right = insert(root.right,x)
            return root
        
        for i in arr:
            root = insert(root,i)
        return root

        

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        q = [root]
        bg =[]
        while(q):
            x =[]
            for i in range(len(q)):
                node = q.pop(0)
                if(node == None):
                    x.append(None)
                    
                    continue
                x.append(node.val)
                q.append(node.left)
                q.append(node.right)

            bg.append(x)
        bg = bg[:-1]
        

        for i in bg[:-1]:
            if(None in i):
                return False
        coun = bg[-1].count(None)
        c =0
        for i in bg[-1][::-1]:
            if(i != None):
                break
            else:
                c +=1
        if(c != coun):
            return False
        return True

                
        

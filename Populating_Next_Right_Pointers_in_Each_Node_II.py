"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        q = [root]
        if(not root):
            return root
        bg = []
        while(q):
            x = []
            for i in range(len(q)):
                node = q.pop(0)
                x.append(node)
                
                if(node.left):
                    q.append(node.left)
                if(node.right):
                    q.append(node.right)
            bg.append(x)
        for i in bg:
            for j in range(len(i) - 1):
                i[j].next = i[j+1]
        
                
        return root

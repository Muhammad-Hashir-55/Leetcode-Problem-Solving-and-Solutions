"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        bg = []
        q = [root]
        if(not root):
            return 0

        while(q):
            x = []
            for i in range(len(q)):
                node = q.pop(0)
                x.append(node.val)
                for j in node.children:
                    q.append(j)
            bg.append(x)
        print(bg)
        n = len(bg)
        return n

        

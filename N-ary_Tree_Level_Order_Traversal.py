"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        bg =[]
        q = [root]
        if(not root):
            return []
        while(q):
            x = []
            
            for i in range(len(q)):
                node = q.pop(0)
                if(node == None):
                    continue
                x.append(node.val)
                if(node.children):
                    xx = node.children
                    for i in xx:
                        q.append(i)
                
            bg.append(x)
            
        return bg
        

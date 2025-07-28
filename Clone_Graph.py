"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        q = [node]
        
        if(None in q):
            
            return node
        
        if(node and node.neighbors == []):
            
            return Node(node.val)
        
        visited = {}
        q = [node]
        visited[node] = Node(node.val)
        while(q):
            nod = q.pop(0)
            for i in nod.neighbors:
                if(i not in visited):
                    visited[i] = Node(i.val)
                    q.append(i)
                
                # real actual sense
                visited[nod].neighbors.append(visited[i])
        
        return visited[node]
        
        

"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        arr = []
        def dfs(root):
            if(root == None):
                return
            arr.append(root.val)
            if(root.child != None):
                dfs(root.child)

            dfs(root.next)
        dfs(head)
        
        head = None
        tail = None
        prev= None
        for i in arr:
            temp = Node(i)
            if(head == None):
                head = temp
                tail = temp
                
            else:
                tail.next = temp
                temp.prev = tail
                tail = temp
        return head

            
        

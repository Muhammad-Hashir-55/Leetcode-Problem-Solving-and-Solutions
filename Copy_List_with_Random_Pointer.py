"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        h = None
        t = None
        iter = head
        while(iter):
            temp = Node(iter.val)
            if(h == None):
                h = temp
                t = temp
            else:
                t.next = temp
                t = temp
            iter = iter.next
        
        dic = {}
        iter = head
        iter1 = h

        while(iter):
            dic[iter] = [iter1 , 0]
            temp = head
            if(iter.random == None):
                dic[iter][1] = None
            else:
                temp = head
                temp1 = h
                while(temp):
                    if(temp == iter.random):
                        iter1.random = temp1
                        break
                    dic[iter][1] +=1
                    temp = temp.next
                    temp1 = temp1.next
            iter = iter.next
            iter1 = iter1.next
        

        


        return h


        


            

        
        

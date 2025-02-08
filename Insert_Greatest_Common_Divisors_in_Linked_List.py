# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from math import gcd
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        temp = head
        while(temp != None):
            arr.append(temp.val)
            temp = temp.next
        n = len(arr)
        if(n ==1):
            return head
        print(arr)

        aaa = []
        aaa.append(arr[0])
        for i in range(n-1):
            y = gcd(arr[i],arr[i+1])
            z = gcd(arr[i+1])
        
            aaa.append(y)
            aaa.append(z)
        
            
        
        head = None
        tail = None
        for i in aaa:
            temp = ListNode(i)
            if(head == None):
                head = temp
                tail = temp
            else:
                tail.next = temp
                tail = temp
        return head
            

        

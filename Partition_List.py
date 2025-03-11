# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        arr = []
        temp = head
        while(temp != None):
            arr.append(temp.val)
            temp = temp.next
        a = []
        for i in arr:
            if(i <x):
                a.append(i)
        for i in arr:
            if(i>=x):
                a.append(i)
        
        head = None
        tail = None
        for i in a:
            temp = ListNode(i)
            if(head == None):
                head = temp
                tail = temp
            else:
                tail.next = temp
                tail = temp
        return head

        

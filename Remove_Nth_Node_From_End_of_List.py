# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = head
        arr = []
        while(temp != None):
            arr.append(temp.val)
            temp = temp.next
        nn = len(arr)
        arr.pop(nn - n)
        head = None
        tail = None
        for i in arr:
            temp = ListNode(i)
            if(head == None):
                head = temp
                tail = temp
            else:
                tail.next = temp
                tail = temp
        return head

        

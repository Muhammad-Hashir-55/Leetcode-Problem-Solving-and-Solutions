# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        arr= []
        temp = head
        while(temp != None):
            arr.append(temp.val)
            temp = temp.next
        arr[k-1],arr[-k] = arr[-k],arr[k-1]
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
        

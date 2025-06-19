# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        arr = []
        temp = head
        while(temp):
            arr.append(temp.val)
            temp = temp.next
        
        bg = []
        
        n = len(arr)
        idx = 0
        while(idx < n):
            x = []
            for j in range(k):
                x.append(arr[idx])
                idx +=1
                if(idx == n):
                    break
            if(len(x) == k):
                x = x[::-1]
            bg.append(x)
        
        final = []
        for i in bg:
            for j in i:
                final.append(j)
        
        head = None
        tail = None
        for i in final:
            temp = ListNode(i)
            if(head == None):
                head = temp
                tail = temp
            else:
                tail.next = temp
                tail = temp
        return head

        

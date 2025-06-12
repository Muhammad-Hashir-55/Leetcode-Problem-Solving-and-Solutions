# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ss = set()
        temp = head
        
        
        ans = None
        while(temp):
            ss.add(temp)
            
            if(temp.next in ss):
                ans = temp.next
                break
            temp = temp.next
            
        return ans

        

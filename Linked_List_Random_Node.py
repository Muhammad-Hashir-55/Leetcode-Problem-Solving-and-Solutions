# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.arr = []
        temp = head
        while(temp):
            self.arr.append(temp.val)
            temp = temp.next
        
        

    def getRandom(self) -> int:
        import numpy as np
        return int(np.random.choice(self.arr))
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        nums = []
        temp = head
        while(temp != None):
            nums.append(temp.val)
            temp = temp.next
        
        n = len(nums)
        if(n ==0):
            return head
        k = k%n

        for i in range(k):
            nums.insert(0,nums[-1])
            nums.pop()
        head = None
        tail = None
        for i in nums:
            temp = ListNode(i)
            if(head == None):
                head = temp
                tail = temp
            else:
                tail.next = temp
                tail= temp
        return head


        

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        arr= []
        temp = head
        ss = set(nums)
        while(temp != None):
            if(temp.val not in ss):
                arr.append(temp.val)
            temp = temp.next
        head = None
        tail = None
        for i in arr:
            temp = ListNode(i)
            if(head == None):
                head = temp
                tail = temp
            else:
                tail.next= temp
                tail = temp
        return head
        

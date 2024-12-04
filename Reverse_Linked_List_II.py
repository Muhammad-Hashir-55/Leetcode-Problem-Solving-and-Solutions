# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def __init__(self):
        self.arr = []
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        temp = head
        while(temp != None):
            self.arr.append(temp.val)
            temp = temp.next
        x = self.arr[left-1:right]
        x.reverse()
        ans = []
        for i in self.arr[:left-1]:
            ans.append(i)
        for i in x:
            ans.append(i)
        for i in self.arr[right:]:
            ans.append(i)
        head = None
        tail = None
        for i in ans:
            temp = ListNode(i)
            if(head == None):
                head = temp
                tail = temp
            else:
                tail.next = temp
                tail = temp
        return head

        

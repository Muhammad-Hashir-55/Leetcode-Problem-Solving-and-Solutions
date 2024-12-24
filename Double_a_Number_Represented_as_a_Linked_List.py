# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        temp = head
        while(temp != None):
            arr.append(temp.val)
            temp = temp.next
        x = []
        carr = 0
        for i in arr[::-1]:

            xx = i*2
            xx +=carr
            carr = 0
            if(xx>=10):
                carr = xx//10
                xx = xx%10
            x.append(xx)
        if(carr >0):
            x.append(carr)
        head = None
        tail = None
        x = x[::-1]
        for i in x:
            temp = ListNode(i)
            if(head == None):
                head = temp
                tail = temp
            else:
                tail.next = temp
                tail = temp
        return head


        

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        sumi = 0
        temp = head
        while(temp != None):
            if(temp.val == 0):
                if(sumi != 0):
                    arr.append(sumi)
                    sumi = 0
            sumi += temp.val
            temp = temp.next
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
        

        

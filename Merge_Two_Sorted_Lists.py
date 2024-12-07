# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        n1 = 0
        n2 = 0
        temp1 = list1
        temp2 = list2
        head = None
        tail = None
        while(temp1 != None and temp2 != None):
            if(temp1.val <= temp2.val):
                temp = ListNode(temp1.val)
                if(head == None):
                    head = temp
                    tail = temp
                else:
                    tail.next = temp
                    tail = temp
                temp1 = temp1.next
                
            else:
                temp = ListNode(temp2.val)
                if(head == None):
                    head = temp
                    tail = temp
                else:
                    tail.next = temp
                    tail = temp
                temp2 = temp2.next
        while(temp1 != None):
            temp = ListNode(temp1.val)

            if(head == None):
                head = temp
                tail = temp
            else:
                tail.next = temp
                tail = temp
            temp1 = temp1.next
        while(temp2 != None):
            temp = ListNode(temp2.val)
            if(head == None):
                head = temp
                tail = temp
            else:
                tail.next = temp
                tail = temp
            temp2 = temp2.next

        return head
            

                    

        

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:

        arr= []
        temp= head
        while(temp):
            arr.append(temp.val)
            temp = temp.next
        print(arr)
        x = []
        maxi = -1
        for i in arr[::-1]:
            maxi = max(maxi,i)
            if(i >= maxi):
                x.append(i)
            else:
                continue
        x = x[::-1]
        head = None
        tail = None

        for i in x:
            temp = ListNode(i)
            if(head == None):
                head = temp
                tail = temp
            else:
                tail.next = temp
                tail = temp
        return head



        

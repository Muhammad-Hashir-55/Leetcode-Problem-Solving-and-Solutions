# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        n = len(lists)
        arr = []
        for i in range(n):
            temp = lists[i]
            while(temp != None):
                arr.append(temp.val)
                temp = temp.next
        arr.sort()
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

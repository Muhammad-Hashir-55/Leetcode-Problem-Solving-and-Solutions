# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        s1 = []
        s2 = set()
        temp = headA
        while(temp):
            s1.append(temp)
            temp = temp.next
        temp = headB
        while(temp):
            s2.add(temp)
            temp = temp.next
        for i in s1:
            if(i in s2):
                return i
        return None

        

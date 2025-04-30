# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        arr = []
        temp = list1
        store = temp
        idx = 0
        
        while(temp != None and idx < a ):
            arr.append(temp.val)
            store = temp.next
            temp = temp.next
            idx +=1
    
        temp = list2
        while(temp != None):
            arr.append(temp.val)
            temp = temp.next
        
        while(store != None and idx <=b):
            store = store.next
            idx +=1
        while(store != None):
            arr.append(store.val)
            store = store.next
        

        list1 = None
        head = None
        tail =None
        for i in arr:
            temp = ListNode(i)
            if(head == None):
                head = temp
                tail = temp
            else:
                tail.next = temp
                tail = temp
        list1 =head
        return list1


        
        

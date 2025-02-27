# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        temp = head
        while(temp != None):
            arr.append(temp.val)
            temp = temp.next
        
        n = len(arr)
        print(arr)
        i = 0
        leng = 1
        a = []
        while(i<n):
            x = []

            for j in range(leng):
                x.append(arr[i])
                i +=1
                if(i>=n):
                    break
            leng +=1
            
            if(len(x) %2 ==0):
                a.append(x[::-1])
            else:
                a.append(x)
        
        aa = []
        n = len(a)
        for i in range(len(a)):
            for j in range(len(a[i])):
                
                aa.append(a[i][j])

        head = None
        tail = None
        for i in aa:
            temp = ListNode(i)
            if(head == None):
                head = temp
                tail= temp
            else:
                tail.next = temp
                tail = temp
        return head
        



        

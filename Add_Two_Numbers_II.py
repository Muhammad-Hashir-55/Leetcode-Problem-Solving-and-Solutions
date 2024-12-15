# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        temp1 = l1
        arr1=  []
        arr2 = []
        while(temp1 != None):
            arr1.append(temp1.val)
            temp1= temp1.next
        temp2 = l2
        while(temp2 != None):
            arr2.append(temp2.val)
            temp2= temp2.next
        arr = []
        n1= len(arr1)
        n2 = len(arr2)
        carr = False
        i = n1-1
        j = n2-1
        while(i>=0 and j >=0):

            x = arr1[i] + arr2[j]
            if(carr ==True):
                x=x +1
                carr= False

            if(x >9):
                x = x%10
                carr = True
            arr.append(x)
            i-=1
            j-=1
        while(i>=0):
            x = arr1[i]
            if(carr ==True):
                x=x +1
                carr= False

            if(x >9):
                x = x%10
                carr = True
            arr.append(x)
            i -=1
        while(j>=0):
            x = arr2[j]
            if(carr ==True):
                x=x +1
                carr= False

            if(x >9):
                x = x%10
                carr = True
            arr.append(x)
            j -=1
        if(carr == True):
            arr.append(1)
            carr = False
        head = None
        tail = None
        for i in arr[::-1]:
            temp = ListNode(i)
            if(head == None):
                head = temp
                tail = temp
            else:
                tail.next = temp
                tail = temp
        return head



        


        
        

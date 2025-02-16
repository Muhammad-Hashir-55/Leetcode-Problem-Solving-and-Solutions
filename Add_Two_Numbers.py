# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        arr1 = []
        temp = l1
        while(temp != None):
            arr1.append(temp.val)
            temp = temp.next
        print(arr1)
        temp = l2
        arr2 = []
        while(temp != None):
            arr2.append(temp.val)
            temp = temp.next
        print(arr2)

        arr = []
        n1 = len(arr1)
        n2 = len(arr2)
        c = False
        carr = 0
        if(n1 <= n2):
            for i in range(n1):
                x = arr1[i] + arr2[i] + carr
                carr = 0
                if(x > 9):
                    c = True
                arr.append(x %10)
                if(c == True):
                    carr = 1
                    c = False
        else:
            for i in range(n2):
                x = arr1[i] + arr2[i] + carr
                carr = 0
                if(x > 9):
                    c = True
                arr.append(x %10)
                if(c == True):
                    carr = 1
                    c = False
        print(carr)
        if(n1 <=n2):
            c = False
            
            for i in range(n1,n2):
                print(arr2[i],carr)
                x = arr2[i] + carr

                carr = 0
                if(x >9):
                    c = True
                arr.append(x %10)
                if(c == True):
                    carr = 1
                    c = False
        else:
            c = False
            
            for i in range(n2,n1):
                x = arr1[i] + carr
                carr = 0
                if(x >9):
                    c = True
                arr.append(x %10)
                if(c == True):
                    carr = 1
                    c = False
        if(carr == 1):
            arr.append(1)
            



        print(arr)
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
                




        

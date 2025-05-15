# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        arr = []
        temp = head
        while(temp):
            arr.append(temp.val)
            temp = temp.next
        
        
        idxs = []
        a = []
        n = len(arr)
        for i in range(1,n-1):
            if(arr[i] > arr[i-1] and arr[i] > arr[i+1]):
                idxs.append(i)
            elif(arr[i] < arr[i-1] and arr[i] < arr[i+1]):
                idxs.append(i)
        if(not idxs or len(idxs) ==1):
            return [-1,-1]
        
        
        
        a.append(-1)
        a.append(idxs[-1] - idxs[0])
        n = len(idxs)
        
        diff = 999999
        for i in range(n-1):
            if(diff > idxs[i+1] - idxs[i]):
                diff = idxs[i+1] - idxs[i]
        
        if(diff != 999999):
            a[0] = diff
        return a

        
        

        

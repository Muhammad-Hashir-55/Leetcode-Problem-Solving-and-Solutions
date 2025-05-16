# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        arr = []
        temp = head
        while(temp):
            arr.append(temp.val)
            temp = temp.next
        n = len(arr)
        tw = []
        for i in range(n):
            if(i>=0 and i <=(n//2) -1):
                tw.append((arr[i], arr[n-1-i]))
        print(tw)
        ss = []
        for i in tw:
            ss.append(sum(i))
        return max(ss)

        

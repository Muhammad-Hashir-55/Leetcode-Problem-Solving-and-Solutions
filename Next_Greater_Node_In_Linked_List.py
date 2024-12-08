# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# important
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        arr = []
        temp = head
        while(temp != None):
            arr.append(temp.val)
            temp = temp.next
        
        n = len(arr)
        stack = []
        ans = [0] *n
        for i in range(n):
            while(stack and arr[i]>arr[stack[-1]]):
                ans[stack.pop()] = arr[i]
            stack.append(i)
        return ans
                
        

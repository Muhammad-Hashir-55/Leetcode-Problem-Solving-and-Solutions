# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        nums = []
        temp = head
        while(temp):
            nums.append(temp.val)
            temp = temp.next
        def mk(nums):
            if(not nums):
                return
            n = len(nums)
            mid = n//2
            root = TreeNode(nums[mid])
            root.left = mk(nums[:mid])
            root.right = mk(nums[mid+1:])
            return root
        root = mk(nums)
        return root
        

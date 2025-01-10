class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        left = []
        right = []
        n = len(nums)
        for i in range(n):
            left.append(sum(nums[:i]))
        # print(left)
        nums = nums[::-1]
        for i in range(n):
            right.append(sum(nums[:i]))
        right = right[::-1]
        arr =[]
        for i in range(n):
            arr.append(abs(left[i]-right[i]))
        return arr

        

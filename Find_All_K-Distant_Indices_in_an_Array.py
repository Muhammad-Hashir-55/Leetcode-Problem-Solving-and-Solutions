class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        n = len(nums)
        keys = []
        for i in range(n):
            if(nums[i] == key):
                keys.append(i)

        
        arr = []
        for i in range(n):
            c = False
            for j in keys:
                if(abs(i - j) <=k):
                    c = True
                    break
            if(c):
                arr.append(i)
        return arr

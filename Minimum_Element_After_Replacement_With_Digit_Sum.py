class Solution:
    def minElement(self, nums: List[int]) -> int:
        arr = []
        for i in nums:
            x = str(i)
            sumi = 0
            for j in x:
                xx = int(j)
                sumi +=xx
            arr.append(sumi)
        return min(arr)

        

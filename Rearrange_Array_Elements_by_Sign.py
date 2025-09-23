class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        arr1 = []
        arr2 = []
        for i in nums:
            if(i  > 0):
                arr1.append(i)
            else:
                arr2.append(i)
        fin = []
        
        n = len(arr1)
        for i in range(n):
            fin.append(arr1[i])
            fin.append(arr2[i])
        return fin

        

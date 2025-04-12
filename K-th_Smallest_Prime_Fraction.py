class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)
        nums = []
        for i in range(n):
            for j in range(i+1,n):
                nums.append(arr[i]/arr[j])
        nums.sort()
        for i in range(n):
            for j in range(i+1,n):
                if(arr[i]/arr[j] == nums[k -1]):
                    return [arr[i] , arr[j]]
        

        
        

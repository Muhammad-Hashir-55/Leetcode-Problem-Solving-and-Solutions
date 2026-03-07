class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        arr = {}
        for i in divisors:
            count = 0
            for j in nums:
                if(j%i == 0):
                    count +=1
            arr[i] = count
        maxi = max(list(arr.values()))
        new_a = []
        for i in arr:
            if(maxi == arr[i]):
                new_a.append(i)
        return min(new_a)
        

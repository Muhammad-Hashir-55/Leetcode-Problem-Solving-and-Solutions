class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        # although it worked but the solution needs to be optimized as
        # it is taking 7 seconds for the time being
        if(n>1):
            if(numbers[-1] + numbers[-2] == target):
                return [n-1,n]
        for i in range(n):
            for j in range(i+1,n):
                if(numbers[i] + numbers[j] == target):
                    return [i+1,j+1]
        

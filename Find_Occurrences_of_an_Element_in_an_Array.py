class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        dic = {}
        n= len(nums)
        for i in range(n):
            if(nums[i] in dic):
                dic[nums[i]].append(i)
            else:
                dic[nums[i]] = [i]
        if(x not in dic):
            return [-1] * len(queries)
        arr = []
        for i in queries:
            if(len(dic[x]) >= i):
                arr.append(dic[x][i-1])
            else:
                arr.append(-1)
        return arr


        

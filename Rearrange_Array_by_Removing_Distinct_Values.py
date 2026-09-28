class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        ans = []
        dic = {}
        for i in nums:
            if(i not in dic):
                dic[i] = 0
            dic[i] +=1
        maxi = max(nums)
        nums.sort()
        while(nums):
            ss = set()
            for i in nums:
                if(i not in ss):
                    ans.append(i)
                ss.add(i)
            for i in ss:
                nums.remove(i)
        return ans
            

        

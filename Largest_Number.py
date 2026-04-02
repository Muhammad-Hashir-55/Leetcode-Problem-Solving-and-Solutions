class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        strs = []
        for i in nums:
            strs.append(str(i))
        num = ''
        while(strs):
            best = strs[0]
            for i in strs:
                if(best + i < i+best):
                    best = i
            num +=best
            strs.remove(best)
        if(num[0] == '0'):
            return '0'
        else:
            return num

        

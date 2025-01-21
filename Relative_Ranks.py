class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        nums = sorted(score,reverse=True)
        n = len(nums)
        dic = {}
        dic[nums[0]] = 'Gold Medal'
        if(n >1):

            dic[nums[1]] = 'Silver Medal'
        if(n >2):

            dic[nums[2]] = 'Bronze Medal'
        x = 4
        for i in nums[3:]:
            dic[i] = str(x)
            x +=1
        arr = []
        for i in score:
            arr.append(dic[i])
        return arr

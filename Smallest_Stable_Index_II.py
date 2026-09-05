class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        pref_maxis = []
        pref_minis = []
        maxi = float('-inf')
        mini = float('inf')
        n = len(nums)
        for i in nums:
            maxi = max(maxi,i)
            pref_maxis.append(maxi)

        for i in nums[::-1]:
            mini = min(mini,i)
            pref_minis.append(mini)
        pref_minis = pref_minis[::-1]

        for i in range(n):
            x = pref_maxis[i] - pref_minis[i]
            if(x <=k):
                return i
        return -1


        

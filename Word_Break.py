class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp =[]
        
        for i in range(n+1):
            dp.append(False)
        
        dp[0] = True
        for i in range(1,n+1):
            for j in range(i):
                if(dp[j] == True and s[j:i] in wordDict):
                    dp[i] = True
                    break
        return dp[-1]
        

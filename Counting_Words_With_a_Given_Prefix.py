class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        ans = 0
        for i in words:
            if(pref in i):
                if(i.index(pref)==0):
                    ans +=1
        return ans
        

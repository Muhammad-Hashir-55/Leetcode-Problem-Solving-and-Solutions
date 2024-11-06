class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        ans = 0
        for i in words:
            if(i  in s):
                if(s.index(i)==0):
                    ans +=1
        return ans

        

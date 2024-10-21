class Solution:
    def sortSentence(self, s: str) -> str:
        s = s.split()
        for i in range(len(s)):
            for j in range(i+1,len(s)):
                if(int(s[i][-1])>int(s[j][-1])):
                    s[i],s[j]= s[j],s[i]
        
        ans = ""
        for k in range(len(s)):
            ans = ans + s[k][:-1] +" "
        return ans[:-1]

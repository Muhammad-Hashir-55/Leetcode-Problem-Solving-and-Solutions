class Solution:
    def reverseByType(self, s: str) -> str:
        s1 = ''
        s2 = ''
        for i in s:
            if(i in "!@#$%^&*()" ):
                s2 +=i
            else:
                s1 +=i
        s1 = s1[::-1]
        s2 = s2[::-1]
        ans = ''
        n = len(s)
        idx1 = 0
        idx2 = 0
        for i in s:
            if(i in "!@#$%^&*()"):
                ans += s2[idx2]
                idx2 +=1
            else:
                ans += s1[idx1]
                idx1 +=1
        return ans

        
        

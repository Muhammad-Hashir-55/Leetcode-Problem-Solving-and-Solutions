class Solution:
    def minimumDeletions(self, s: str) -> int:
        n = len(s)
        res = n
        a = 0
        b = 0
        for i in s:
            if(i == 'a'):
                a +=1
        for i in s:
            if(i == 'a'):
                a -=1
            res = min(res, a+ b)
            if(i == 'b'):
                b +=1
        return res
        

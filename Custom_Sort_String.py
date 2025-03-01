class Solution:
    def customSortString(self, order: str, s: str) -> str:
        ss = ''
        for i in order:
            if(i not in s):
                continue
            n = s.count(i)
            for j in range(n):
                ss +=i
                s = s.replace(i,'',1)
        for i in s:
            ss +=i
        
        return ss
        

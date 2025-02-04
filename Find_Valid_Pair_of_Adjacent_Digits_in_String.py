class Solution:
    def findValidPair(self, s: str) -> str:
        n  =len(s)
        for i in range(n-1):
            ss = s[i] + s[i+1]
            if(ss[0]== ss[1]):
                continue
            if(int(ss[0])== s.count(ss[0]) and int(ss[1]) == s.count(ss[1])):
                return ss
        return ''

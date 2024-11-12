class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        if(len(s)<=3):
            m_set = set(s)
            if(len(s)==len(m_set) and len(m_set)==3):
                return 1
            else:
                return 0
        ii = 0
        iii = 2
        out = 0
        while(iii<len(s)):
            ss = s[ii:iii+1]
            m_set = set(ss)
            if(len(ss)==len(m_set)):
                out +=1
            ii +=1
            iii +=1
        return out


        

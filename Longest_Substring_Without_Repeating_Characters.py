class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if(s ==''):
            return 0
        if(not s):
            return 0
        if(len(s)==1):
            return 1
        ss = []
        ii = 0
        n = len(s)
        
        while(ii != n):
            sss = ""
            for i in range(ii,n):
                if(s[i] not in sss):
                    sss += s[i]
                else:
                    break
            ss.append(sss)
            ii +=1
    
        maxi =len(ss[0])
        for i in ss[1:]:
            if(len(i)>maxi):
                maxi = len(i)
                
        return maxi

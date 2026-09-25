class Solution:
    def longestPalindrome(self, s: str) -> int:
        dic = {}
        for i in s:
            if(i not in dic):
                dic[i] = 0
            dic[i] +=1
        l = 0
        c = False
        for i in dic:
            if(dic[i] %2 ==0):
                l +=dic[i]
            else:
                l += dic[i] -1
                c = True
        if(c):
            f = l +1
        else:
            f = l
        return f
        

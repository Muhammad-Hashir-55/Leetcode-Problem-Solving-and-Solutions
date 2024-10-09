class Solution:
    def longestPalindrome(self, s: str) -> str:

        if(len(s)==1):
            return s

        if(len(s)==2):
            if(s == s[::-1]):
                return s
            else:
                return s[0]
        
        longest = s[0]
        k = len(s)



        for i in range(len(s)):
            n= k
            
            while(n>i+1):
                ss = s[i:n]
                if(ss == ss[::-1]):
                    if(len(ss)>len(longest)):
                        longest =ss
                n -=1
        return longest

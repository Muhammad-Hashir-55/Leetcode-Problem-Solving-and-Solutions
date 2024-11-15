class Solution:
    def modifyString(self, s: str) -> str:
        if('?'not in s):
            return s
        if(len(s)==1 and s[0]=='?'):
            return "a"
        lis = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        n = len(s)
        if(s[0]== '?'):
            for i in lis:
                if(i != s[1]):
                    s = s.replace(s[0],i,1)
                    break
        for i in range(1,n-1):
            if(s[i]=='?'):
                for j in lis:
                    if(j != s[i-1] and j != s[i+1]):
                        s = s.replace(s[i],j,1)
                        break
        if(s[n-1]== "?"):
            for i in lis:
                if(i != s[-2]):
                    s = s.replace(s[-1],i,1)
                    break
        return s





        

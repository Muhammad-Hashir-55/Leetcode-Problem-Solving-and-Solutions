class Solution:
    def capitalizeTitle(self, title: str) -> str:
        l = title.split()
        n = len(l)
        for i in range(n):
            if(len(l[i])<=2):
                l[i]= l[i].lower()
            else:
                l[i]= l[i].capitalize()
        ans=  ""
        ans = (" ").join(l)
        return ans
        
        

        

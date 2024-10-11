class Solution:
    def shortestCompletingWord(self, licensePlate: str, words) -> str:
        s = ""
        for i in licensePlate:
            if(i.isalpha()):
                s = s + i.lower()
        new_list = []
        for j in words:
            c = False
            for k in s:
                    if(s.count(k)<= j.count(k)):
                        c = True
                    else:
                       
                       c= False
                       break
                        
            
            if(c== True):
                new_list.append(j)
        
        if(new_list):
            ans = new_list[0]
            for i in new_list[1:]:
                if(len(i)<len(ans)):
                    ans= i
            return ans
        else:
            return ""

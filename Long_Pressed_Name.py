class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        if(name == typed):
            return True
        s = ''
        ii =0
        n = len(name)

        for i in typed:
            if(i ==name[ii] and s != name):
                s +=i

                if(ii<n -1):
                    ii +=1
            if(s == name and i !=s[-1]):
                return False
        n = len(typed)
        if(n>1):
            for i in range(n-1):
                if(typed[i]+typed[i+1] not in name and typed[i] != typed[i+1]):
                    return False
            
        if(s == name):
            return True
        else:
            return False

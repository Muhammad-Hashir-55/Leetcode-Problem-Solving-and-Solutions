class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dic1 = {}
        for i in magazine:
            if(i not in dic1):
                dic1[i] = 1
            else:
                dic1[i] +=1
        dic2 = {}
        for i in ransomNote:
            if(i not in dic2):
                dic2[i] = 1
            else:
                dic2[i] +=1
        
        for i in dic2:
            if(i not in dic1):
                return False
            elif(dic1[i]<dic2[i]):
                return False
        return True

        

class Solution:
    def reportSpam(self, message: List[str], bannedWords: List[str]) -> bool:
        dic = {}
        for i in bannedWords:
            if(i not in dic):
                dic[i] = 1
        c = 0
        for i in message:
            if(i in dic):
                c +=1
            if(c ==2):
                return True
        return False

        

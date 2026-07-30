class Solution:
    def minimumPushes(self, word: str) -> int:
        n = len(word)
        if(n <=8):
            return n
        
        add = 0
        count = 0
        for i in range(n):
            if(i % 8 == 0):
                add +=1
            count +=add
        return count


        

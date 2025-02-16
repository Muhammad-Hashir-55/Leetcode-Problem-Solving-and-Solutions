class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        alphas = 'abcdefghijklmnopqrstuvwxyz'
        c = 0
        for i in alphas:
            if(i in word and i.upper() in word):
                c +=1
        return c

        

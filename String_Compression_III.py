class Solution:
    def compressedString(self, word: str) -> str:
        comp = ""
        while(word):
            s = word[0]
            for i in word[1:]:
                if(s[0] == i and len(s)<9):
                    s += i
                else:
                    break
            comp += str(len(s)) + s[0]
            word = word.replace(s,"",1)
        return comp
        

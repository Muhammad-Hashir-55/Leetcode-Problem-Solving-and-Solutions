class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        nn = len(words[0])
        n = len(s)
        arr = []
        total = nn * len(words)
        idx = 0
        
        while(idx + total <= n):
            x = words[:]
            word = s[idx:idx + nn]
            c = False
            idx_c = idx
            while(word in x):
                x.remove(word)
                idx_c +=nn
                word = s[idx_c:idx_c + nn]
                if(not x):
                    c = True
                    break
            if(c == True):
                arr.append(idx)
            idx +=1
        return arr




        

class Solution:
    def shortestToChar(self, s: str, c: str) -> list[int]:
        idxs = []
        n = len(s)
        for i in range(n):
            if(s[i] == c):
                idxs.append(i)
        arr = []
        idx = 0
        for i in s:
            if(i == c):
                arr.append(0)
            else:
                mini = float('inf')
                for j in idxs:
                    mini = min(abs(idx-j),mini)
                arr.append(mini)
            idx +=1
        return arr
        

class Solution:
    def divideString(self, s: str, k: int, fill: str) -> list[str]:
        arr = []
        n = len(s)
        c = True
        for i in range(0,n,k):
            idx = i+k
            x = s[i:idx]
            if(len(x) == k):
                arr.append(x)
            else:
                c = False
                break
                
        if(c == False):
            while(len(x) != k):
                x +=fill
            arr.append(x)
        return arr

        

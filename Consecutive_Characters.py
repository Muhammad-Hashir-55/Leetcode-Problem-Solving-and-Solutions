class Solution:
    def maxPower(self, s: str) -> int:
        i = 0
        n = len(s)
        arr = []
        if(n ==1):
            return 1
        while(i<n):
            store = s[i]
            c= 0

            while(s[i]==store):
                

                c +=1
                i+=1
                if(i ==n):
                    break
            arr.append(c)
        return max(arr)
        

class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        req = 2*k
        store = req
        arr = []
        for i in s:
            arr.append(i)
        
        n = len(arr)
        bg = []
        idx = 0
        while(True):
            if(idx >=n):
                break
            if(req >=n):
                x = arr[idx:]
                
            else:
                x = arr[idx:req]
            idx = req
            req += store
            

            if(len(x) == store):
                bg.append(x[:k][::-1])
                bg.append(x[k:])
            elif(len(x) < store and len(x)>= k):
                bg.append(x[:k][::-1])
                bg.append(x[k:])
            else:
                bg.append(x[::-1])
        fin = ''
        for i in bg:
            for j in i:
                fin +=j
        return fin
        

        

class Solution:
    def printVertically(self, s: str) -> List[str]:
        k = s.split(' ')
        n = len(k)
        m = -1
        for i in k:
            if(len(i)>m):
                m = len(i)
    
        arr = []
        
        for i in range(m):
            s= ''
            for j in range(n):
                if(i>= len(k[j])):
                    s +=' '
                    continue
                s += k[j][i]
                
            arr.append(s)
        n = len(arr)
        for i in range(n):
            while(arr[i][-1] == ' '):
                arr[i] = arr[i][:-1]
        return arr
                
        

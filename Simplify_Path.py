class Solution:
    def simplifyPath(self, path: str) -> str:
        while('//' in path):
            path = path.replace('//','/')
        
        if(path[-1]=='/'):
            path = path[:-1]
        
        k = path.split('/')
        new_k = []
        for i in k:
            if(i ==  '.'):
                continue
            new_k.append(i)
        k = new_k
        

        while('..' in k):
            idx = k.index('..')
            k.pop(idx)
            if(idx == 0):
                continue
            k.pop(idx-1)

        

        s = '/'
        for i in k:
            if(not i):
                continue
            elif(i=='.'):
                continue
            else:
                s +=i
            s +='/'
        s = s[:-1]
        if(not s):
            return '/'
        return s
        

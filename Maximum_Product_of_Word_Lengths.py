class Solution:
    def maxProduct(self, words: List[str]) -> int:
        n = len(words)
        maxi = 0
        for i in range(n):
            for j in range(i+1,n):
                x1 = set(words[i])
                x2 = set(words[j])
                comm = False
                for k in x1:
                    if(k in x2):
                        comm = True
                        break
                if(comm == False):
                    for l in x2:
                        if(l in x1):
                            comm= True
                            break
                if(comm == False):
                    a = len(words[i]) *len(words[j])
                    if(a>maxi):
                        maxi = a
        return maxi
                    
        

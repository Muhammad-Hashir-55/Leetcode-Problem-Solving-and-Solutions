class Solution:
    def minTimeToType(self, word: str) -> int:
        alphas = 'abcdefghijklmnopqrstuvwxyz'
        alphas += alphas
        total = 0
        letter = 'a'
        for i in word:
            idxs = []
            
            for j in range(len(alphas)):
                if(alphas[j] == letter):
                    idxs.append(j)
        
            for j in range(len(alphas)):
                if(alphas[j]== i):
                    idxs.append(j)

            
            idxs.sort()
    
            mini = inf
            for j in range(1,len(idxs)):
                x = idxs[j] - idxs[j-1]
                if(x < mini):
                    mini = x
            letter = i
            total += mini
            total +=1
    
        return total

            

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: list[str]) -> int:
        if(endGene not in bank):
            return -1
        q = [startGene]
        if(startGene == endGene):
            return 0
        if(startGene in bank):
            bank.remove(startGene)
        steps =1
        while(q):
            n = len(q)
            for i in range(n):
                x = q.pop(0)
                for j in bank.copy():
                    count = 0

                    for k in range(8):
                        if(x[k] != j[k]):
                            count +=1
                    
                    if(count == 1):
                        if(endGene == j):
                            return steps
                        q.append(j)
                        bank.remove(j)
                        
            steps +=1
        return -1
            
                
        

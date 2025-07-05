from itertools import combinations
class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        kk = k
        bg = []
        for i in range(1,n+1):
            x = list(combinations(nums,i))
            bg.extend(x)
        final = []
        for i in bg:
            if(len(i) == 1):
                final.append(i)
            else:
                cont = False
                for j in range(len(i)):
                    for k in range(j+1,len(i)):
                        if(abs(i[k] - i[j]) == kk):
                            cont = True
                            break
                    if(cont == True):
                        break
                
                if(cont == True):
                    continue
                else:
                    final.append(i)
                    
        
        return len(final)

        

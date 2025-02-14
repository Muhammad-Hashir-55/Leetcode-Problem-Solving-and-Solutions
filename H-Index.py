class Solution:
    def hIndex(self, citations: List[int]) -> int:
        c= 0
        citations.sort(reverse= True)
        print(citations)
        for i,j in enumerate(citations):
            
            if(i +1 <=j):
                c +=1
            else:
                break
            # print('right now c is',c)
        return c

        

class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        comm = []
        for i in range(1,n+1):
            x1 = A[:i]
            x2 = B[:i]
            c = 0
            for j in x1:
                if(j in x2):
                    c +=1
            comm.append(c)
        return comm


        

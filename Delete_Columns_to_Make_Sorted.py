class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs)
        m = len(strs[0])
        bg = []
        for i in range(m):
            s = []
            for j in range(n):
                s.append(strs[j][i])
            bg.append(s)
        
        count = 0
        for i in bg:
            if(sorted(i) != i):
                count +=1
        return count


        

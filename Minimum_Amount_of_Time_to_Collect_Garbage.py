class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        n = len(garbage)
        tot = 0
        arr=garbage[:][::-1]
        m_idx = n
        for j in range(n):
            if('M' in arr[j]):
                break
            
            m_idx -=1
        
        p_idx = n
        for j in range(n):
            if('P' in arr[j]):
                break
            p_idx -=1
        
        g_idx = n
        for j in range(n):
            if('G' in arr[j]):
                break
            g_idx -=1
        
        
        
        i =0
        for i in range(m_idx):
            if('M' in garbage[i]):
                count = garbage[i].count('M')
                tot +=count
            
        tot += sum(travel[:i])
        


        i=0
        for i in range(p_idx):
            if('P' in garbage[i]):
                count = garbage[i].count('P')
                tot +=count
            
        tot += sum(travel[:i])
        


        i=0
        for i in range(g_idx):
            if('G' in garbage[i]):
                count = garbage[i].count('G')
                tot +=count
            
        tot += sum(travel[:i])
      



        return tot



        

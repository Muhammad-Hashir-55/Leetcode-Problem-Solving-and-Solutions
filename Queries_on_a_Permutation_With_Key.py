class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        arr = []
        p = []
        for i in range(1,m+1):
            p.append(i)
        for i in queries:
            idx = p.index(i)
            arr.append(idx)
            p.pop(idx)
            p.insert(0,i)
            
        return arr
        

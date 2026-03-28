class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        visited = set()
        for i in edges:
            visited.add(i[1])
        arr = []
        for i in range(0,n):
            if(i not in visited):
                arr.append(i)
        return arr
        

        

class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        arr = []
        for i in matrix:
            x = i.count(1)
            arr.append(x)
        return arr
        

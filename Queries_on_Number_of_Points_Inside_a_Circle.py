class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        arr = []
        for i in queries:
            coun = 0
            for j in points:
                if(sqrt((i[0] - j[0])**2 + (i[1] - j[1])**2) <=i[2]):
                    coun +=1
            arr.append(coun)
        return arr
        

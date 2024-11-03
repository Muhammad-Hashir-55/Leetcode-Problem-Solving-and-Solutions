class Solution:
    def nearestValidPoint(self, x: int, y: int, points) -> int:
        new_list = []
        for i in points:
            if(i[0]==x or i[1]==y):
                lis = []
                lis.append((abs(x - i[0])+ abs(y - i[1])))
                lis.append(points.index(i))
                new_list.append(lis)
        if(not new_list):
                return -1
        
        new_list.sort()
        return new_list[0][1]

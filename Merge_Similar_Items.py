class Solution:
    def mergeSimilarItems(self, items1: list[list[int]], items2: list[list[int]]) -> list[list[int]]:
        dic = {}
        for i in items1:
            if(i[0] not in dic):
                dic[i[0]] = i[1]
            else:
                dic[i[0]] += i[1]
        
        for i in items2:
            if(i[0] not in dic):
                dic[i[0]] = i[1]
            else:
                dic[i[0]] += i[1]
        
        arr = []
        for i in dic:
            x = [i,dic[i]]
            arr.append(x)
        
        arr.sort()
        return arr
        
        

class Solution:
    def countPoints(self, rings: str) -> int:
        dic = {}
        n = len(rings)
        for i in range(1,n,2):
            if(rings[i] not in dic):
                dic[rings[i]] = set()
            dic[rings[i]].add(rings[i-1])
        
        count = 0
        for i in dic:
            if(len(dic[i]) ==3):
                count +=1
        return count
        

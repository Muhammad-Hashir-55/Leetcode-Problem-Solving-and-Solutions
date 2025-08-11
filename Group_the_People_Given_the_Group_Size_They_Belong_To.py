class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        dic = {}
        n= len(groupSizes)

        for i in range(n):
            if(groupSizes[i] not in dic):
                dic[groupSizes[i]] = []
                x = [i]
                dic[groupSizes[i]].append(x)
            else:
                if(len(dic[groupSizes[i]][-1]) == groupSizes[i] ):
                    x = [i]
                    dic[groupSizes[i]].append(x)
                else:
                    dic[groupSizes[i]][-1].append(i)
        
        bg = []
        for i in range(501):
            if(i not in dic):
                continue
            else:
                for j in dic[i]:
                    bg.append(j)
        return bg

        

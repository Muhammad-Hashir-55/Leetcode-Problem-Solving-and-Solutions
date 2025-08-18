class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        dic = {}
        for i in edges:
            if(i[0] not in dic):
                dic[i[0]] = [i[1]]
            else:
                dic[i[0]].append(i[1])
            if(i[1] not in dic):
                dic[i[1]] = [i[0]]
            else:
                dic[i[1]].append(i[0])
        maxi = 0
        for i in dic:
            if(len(dic[i]) > maxi):
                maxi = len(dic[i])
        for i in dic:
            if(len(dic[i]) == maxi):
                return i

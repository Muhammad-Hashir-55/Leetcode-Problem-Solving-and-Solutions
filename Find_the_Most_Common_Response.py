class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        resp = []
        for i in responses:
            ss = set()
            x = []
            for j in i:
                if(j not in ss):
                    ss.add(j)
                    x.append(j)
            resp.append(x)
        dic = {}
        for i in resp:
            for j in i:
                if(j not in dic):
                    dic[j] =1
                else:
                    dic[j] +=1
        maxi = -1
        for i in dic:
            if(dic[i] > maxi):
                maxi = dic[i]
        arr = []
        for i in dic:
            if(maxi == dic[i]):
                arr.append(i)
        arr.sort()
        return arr[0]

        

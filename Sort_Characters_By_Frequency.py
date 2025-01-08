class Solution:
    def frequencySort(self, s: str) -> str:
        dic = {}
        for i in s:
            if(i not in dic):
                dic[i] = 1
            else:
                dic[i] +=1
        k = list(dic.values())
        k.sort(reverse = True)
        s = ""
        while(True):
            for i in dic:
                if(dic[i]==k[0]):
                    for j in range(k[0]):
                        s +=i
                    del dic[i]
                    k.pop(0)
                    break
            if(not dic):
                break
        return s

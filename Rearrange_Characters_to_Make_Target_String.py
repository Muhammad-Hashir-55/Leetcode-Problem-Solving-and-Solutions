class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        arr = []
        dic = {}
        for i in target:
            if(i in dic):
                dic[i] +=1
            else:
                dic[i] =1
        print(dic)
        for i in dic:
            arr.append(s.count(i) // dic[i])
        
        print(arr)   
        return min(arr)     

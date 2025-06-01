class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        arr = []
        dic =  {}
        for i in names:
            if(i not in dic):
                arr.append(i)
                dic[i] = 1
            else:
                num = dic[i]
                name = i + '(' + str(num) + ')'
                while(name in dic):
                    num +=1
                    name = i + '(' + str(num) + ')'
                dic[name] =1
                arr.append(name)
                dic[i] = num 
        return arr
        

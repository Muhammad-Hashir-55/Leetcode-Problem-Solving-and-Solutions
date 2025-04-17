class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        arr = []
        dic = dictionary
        k = sentence.split(' ')
        for i in k:
            x = []
            for j in dic:
                if(j in i and i.index(j) == 0):
                    x.append(j)
            if(not x):
                arr.append(i)
                continue
                
            mini = len(x[0])

            
            for j in x[1:]:
                if(len(j) < mini):
                    mini = len(j)
            for j in x:
                if(len(j) == mini):
                    arr.append(j)
                    break
        s = arr[0]

        for i in arr[1:]:
            s = s + ' ' + i
        return s

        

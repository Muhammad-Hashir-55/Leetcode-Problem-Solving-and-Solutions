class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        arr= []
        n = len(queries)
        for i in range(n):
            x = min(queries[i])
            c = queries[i].count(x)
            coun = 0
            for j in words:
                xx = min(j)
                cc = j.count(xx)
                if(cc>c):
                    coun +=1
            arr.append(coun)
        return arr

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        arr = []
        s = 'abcdefghijklmnopqrstuvwxyz'
        for i in s:
            mini = 999999999
            for j in words:
                mini = min(mini,j.count(i))
            if(mini >0):
                for k in range(mini):
                    arr.append(i)
        return arr


        

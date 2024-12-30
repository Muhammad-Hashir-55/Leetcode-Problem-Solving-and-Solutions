class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        arr = []
        ii = 0
        for i in words:
            if(x in i):
                arr.append(ii)
            ii +=1
        return arr

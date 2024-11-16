class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        maxi =-1
        for i in sentences:
            s = i.split(" ")
            n = len(s)
            if(n>maxi):
                maxi = n
        return maxi
        

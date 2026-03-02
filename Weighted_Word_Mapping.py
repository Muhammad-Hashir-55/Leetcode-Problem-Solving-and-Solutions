class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        strings = 'abcdefghijklmnopqrstuvwxyz'
        dic = {}
        n = 26
        for i in range(n):
            dic[strings[i]] = weights[i]
        wordss = ''
        strings = strings[::-1]
        for i in words:
            z = 0
            for j in i:
                z += dic[j]
            z = z%26
            wordss += strings[z]
        return wordss



        

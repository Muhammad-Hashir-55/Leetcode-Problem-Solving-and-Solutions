class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        sentence = sentence.split(" ")
        n = len(searchWord)
        for i in sentence:
            if(searchWord == i[:n]):
                return sentence.index(i) +1
        return -1
        

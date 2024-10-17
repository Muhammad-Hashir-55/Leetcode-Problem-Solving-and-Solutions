class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        for i in word:
            if(i.isalpha()):
                word = word.replace(i," ")
        word = word.split()
        for j in range(len(word)):
            word[j] = int(word[j])
        seen = set()
        for i in word:
            seen.add(i)
        return len(seen)
        

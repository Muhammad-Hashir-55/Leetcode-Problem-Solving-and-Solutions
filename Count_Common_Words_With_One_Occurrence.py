class Solution:
    def countWords(self, words1, words2) -> int:
        ans = 0
        s = set()
        for i in words1:
            if(words1.count(i)==1 and i in words2 and words2.count(i)==1):
                s.add(i)
        for j in words2:
            if(words2.count(j)==1 and j in words1 and words1.count(j)==1):
                s.add(j)
        return len(s)

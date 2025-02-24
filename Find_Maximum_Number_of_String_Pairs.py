class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        paired = []
        c =0
        n = len(words)
        for i in range(n):
            for j in range(i+1,n):
                if(words[j] not in paired and words[i] == words[j][::-1]):
                    c +=1
                    paired.append(words[j])
        return c

        

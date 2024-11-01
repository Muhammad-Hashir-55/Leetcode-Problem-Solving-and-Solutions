class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        if(word not in sequence):
            return 0
        count = 0
        s = word
        while(s in sequence):
            if(s in sequence):
                count +=1
            s +=word
        return count
        

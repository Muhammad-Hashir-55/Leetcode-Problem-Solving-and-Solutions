class Solution:
    def divisibilityArray(self, word: str, m: int) -> List[int]:
        rem , arr , word =0  , [], map(int,word)
        for i in word:
            rem = (rem * 10 + i) %m

            arr.append(bool(rem)^1)
        return arr 
        

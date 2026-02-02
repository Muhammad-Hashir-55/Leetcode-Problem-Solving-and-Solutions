class Solution:
    def reversePrefix(self, s: str, k: int) -> str:
        ss = s[:k][::-1]
        ss += s[k:]
        return ss
        

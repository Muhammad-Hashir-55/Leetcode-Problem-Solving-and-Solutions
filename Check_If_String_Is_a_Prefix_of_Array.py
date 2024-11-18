class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        ss = ""
        if(s == ss):
            return True
        for i in words:
            ss += i
            if(s ==ss):
                return True
        return False
        

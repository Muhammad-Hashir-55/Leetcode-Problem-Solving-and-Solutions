class Solution:
    def countValidPrefixes(self, s: str) -> int:
        count = 0

        n = len(s)
        from collections import Counter
        x = ''
        for i in s:
            x +=i
            dic = Counter(x)
            x1 = dic.get('1',0)
            x2 = dic.get('0',0)
        
            if(abs(x1-x2) <=1):
                count +=1
        return count


            
        

class Solution:
    def sortVowels(self, s: str) -> str:
        upper = []
        s = list(s)
        lower = []
        n = len(s)
        for i in range(n):
            if(s[i] in 'AEIOU'):
                upper.append(s[i])
                s[i] = '_'
            elif(s[i] in 'aeiou'):
                lower.append(s[i])
                s[i] = '_'
        upper.sort()
        lower.sort()
        if('_' not in s):
            return ('').join(s)
        else:
            for i in range(n):
                if(s[i] == '_'):
                    if(upper):
                        s[i] = upper.pop(0)
                    elif(lower):
                        s[i] = lower.pop(0)
        
        return ('').join(s)


        

class Solution:
    def finalString(self, s: str) -> str:
        final = ''
        for i in s:
            if(i == 'i'):
                final = final[::-1]
            else:
                final +=i
        return final
        

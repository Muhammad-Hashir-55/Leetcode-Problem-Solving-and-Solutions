class Solution:
    def rearrangeString(self, s: str, x: str, y: str) -> str:
        check1 = False
        if(y in s):
            check1 = True
        check2 = False
        if(x in s):
            check2 = True
        var1,var2 = 0,0
        if(check1):
            var1 = s.count(y)
        if(check2):
            var2 = s.count(x)
        f = ''
        f += y*var1
        f += x*var2
        for i in s:
            if(i == y or i == x):
                continue
            f +=i
        return f

        

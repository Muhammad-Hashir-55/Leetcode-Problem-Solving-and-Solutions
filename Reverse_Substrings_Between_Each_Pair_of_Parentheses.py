class Solution:
    def reverseParentheses(self, s: str) -> str:
        s = list(s)
        while(True):
            if(')' in s):
                idx = s.index(')')
                x = idx-1
                stri = ''
                while(s[x] != '('):
                    stri +=s[x]
                    x -=1
                print(x,idx)
                xx= x+1
                for j in stri:
                    s[xx] = j
                    xx +=1
                s.pop(idx)
                s.pop(x)
            else:
                break
        return ''.join(s)
        

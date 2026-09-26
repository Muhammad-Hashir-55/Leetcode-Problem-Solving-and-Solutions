class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        dic = {}
        for i in knowledge:
            dic[i[0]] = i[1]
        ans = ''
        n = len(s)
        st = False
        for i in range(n):
            if(st == False and s[i] != '('):
                ans += s[i]
            elif(s[i] == '('):
                st = True
                key = ''
            elif(st and s[i] != ')'):
                key += s[i]
            else:
                if(key in dic):
                    ans += dic[key]
                else:
                    ans += '?'
                key = ''
                st = False
        return ans
        

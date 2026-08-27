class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        st = [s]
        sett = set()
        n = len(s)
        while(st):
            curr = st.pop()
            if(curr in sett):
                continue
            sett.add(curr)
            
            ss = ''
            for i in range(n):
                if(i %2 ==0):
                    ss += curr[i]
                else:
                    x = int(curr[i])
                    x +=a
                    x = x%10
                    ss += str(x)
            st.append(ss)
        
            for i in range(b):
                x = curr[-1]
                curr = curr[:-1]
                curr = x + curr
            st.append(curr)
            
        return min(sett)


        

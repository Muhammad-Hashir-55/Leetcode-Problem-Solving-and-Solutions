class Solution:
    def calculate(self, s: str) -> int:
        num = 0
        st = []
        p = '+'
        s +='+'
        for i in s:
            if(i.isdigit()):
                num = num *10 + int(i)
            elif(i == ' '):
                continue
            else:
                if(p =='+' ):
                    st.append(num)
                elif(p == '-'):
                    st.append(-num)
                elif(p == '*'):
                    x = st.pop()
                    st.append(x * num)
                else:
                    x= st.pop()
                    st.append(int(x/num))
                p = i
                num = 0
        return sum(st)
        

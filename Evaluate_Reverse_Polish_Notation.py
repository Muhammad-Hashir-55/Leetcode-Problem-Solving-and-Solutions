class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = ['+','-','*','/']
        res = 0
        st = []
        for i in tokens:
            if(i not in ops):
                st.append(i)
            else:
                op = i
                op1 = st.pop()
                op2 = st.pop()
                if(op == '+'):
                    st.append(int(op1) + int(op2))
                elif(op == '-'):
                    st.append(int(op2) - int(op1))
                elif(op == '*'):
                    st.append(int(op1) * int(op2))
                else:
                    st.append(int(int(op2) / int(op1)))
            
        return int(st[-1])
                    

        

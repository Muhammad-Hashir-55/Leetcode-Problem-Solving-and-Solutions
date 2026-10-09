class Solution:
    def minInsertions(self, s: str) -> int:
        st = []
        n = len(s)
        ans = 0
        i = 0
        while(i<n):
            if(s[i] == '('):
                st.append('(')
            elif(s[i] == ')'):
                if(st):
                    if(i+1 >=n):
                        st.append(s[i])
                        break
                    if(s[i+1] == ')'):
                        st.pop()
                        i +=1
                    else:
                        ans +=1
                        st.pop()
                        st.append('(')
                        i +=1
                else:
                    if(i+1 >=n):
                        st.append(s[i])
                        break
                    if(s[i+1] == ')'):
                        ans +=1
                        i +=1
                    else:
                        ans +=2
                        i +=1
                        st.append('(')
            i +=1
    
        if(not st):
            return ans
        else:
            z = st[0]
            if(z == '('):
                x = 2
                for i in st[1:]:
                    if(i == ')'):
                        x -=1
                    elif(i == '('):
                        x +=2
                ans +=x
            elif(z == ')'):
                x = 2
                for i in st[1:]:
                    if(i == ')'):
                        x -=1

                ans +=x
            return ans


                
        

                
        

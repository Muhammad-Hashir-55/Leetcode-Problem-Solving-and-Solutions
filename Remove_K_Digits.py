class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        st = []
        for i in num:
            while(k > 0 and st and st[-1] > i):
                k -=1
                st.pop()
            st.append(i)
        while(k > 0):
            st.pop()
            k -=1
        ans = ''.join(st).lstrip('0')
        if(ans):
            return ans
        else:
            return '0'
        

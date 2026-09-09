class Solution:
    def countCommas(self, n: int) -> int:
        if(n <=999):
            return 0
        tot = 0
        st = 1000
        while(st <= n):
            tot += n- st +1
            st *=1000
        return tot
        

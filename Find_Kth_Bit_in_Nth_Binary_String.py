class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        s = '0'
        for i in range(n-1):
            inv = ''
            for j in s:
                if(j =='1'):
                    inv +='0'
                else:
                    inv += '1'
            rev = inv[::-1]
            s = s + '1' + rev
        
        
        return s[k-1]
        

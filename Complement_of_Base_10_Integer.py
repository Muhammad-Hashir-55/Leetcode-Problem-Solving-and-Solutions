class Solution:
    def bitwiseComplement(self, n: int) -> int:
        s = bin(n)
        s = s[2:]
        new_string= ""
        for i in s:
            if(i =='0'):
                new_string = new_string + '1'
            else:
                new_string = new_string + '0'
        i = len(new_string)
        ii = len(new_string) -1
        poww = 0
        ans = 0
        while(i !=0):
            if(new_string[ii] == '1'):
                ans = ans + 2**poww
            i -=1
            ii -=1
            poww +=1
        return ans

        

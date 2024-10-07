class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        poww = 0
        my_num = 1
        while(my_num<=n):
            my_num = 3 ** poww
            poww +=1
            if(my_num == n):
                return True
            continue
        return False
        

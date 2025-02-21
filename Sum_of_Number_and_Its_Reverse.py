class Solution:
    def sumOfNumberAndReverse(self, num: int) -> bool:
        if(num == 0): # edge case which must needs to be handled
            return True
        for i in range(num):
            s1 = str(i)
            s2 = s1[::-1]
            if(int(s1) + int(s2) == num):
                return True
        else:
            return False
            

        

class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if(num in range(0,10)):
            return num
        result = num

        num = str(num)
        new_list = []
        
        while(result >10):
            
            for i in num:
                new_list.append(int(i))
            result = 0
            for j in new_list:
                result = result + j
            if (result > 10):
                num = str(result)
                new_list = []
            
        if(result == 10):
            return 1
        else:
            return result


check = Solution()
print(check.addDigits(14))

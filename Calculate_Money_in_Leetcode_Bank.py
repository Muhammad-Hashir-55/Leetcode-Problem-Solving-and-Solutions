class Solution(object):
    def totalMoney(self, n):
        """
        :type n: int
        :rtype: int
        """
        day = 1
        sum = 0
        iterator = 1
        monday = 1
        while(day <=n):
            if(day % 7 ==1 ):
                iterator = monday
                monday+=1
            sum = sum + iterator
            iterator +=1
            day +=1
        return sum

        

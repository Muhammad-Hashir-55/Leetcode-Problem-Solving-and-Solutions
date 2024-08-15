class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        my_array= []
        for i in range(len(bills)):
            if(bills[i] == 5):
                my_array.append(bills[i])
            elif(bills[i] == 10):
                my_array.append(bills[i])
                if(5 in my_array):
                    my_array.remove(5)
                else:
                    return False
            elif(bills[i] == 20):
                if((5 in my_array) and (10 in my_array)):
                    my_array.remove(5)
                    my_array.remove(10)
                elif(my_array.count(5) >=3):
                    my_array.remove(5)
                    my_array.remove(5)
                    my_array.remove(5)
                else:
                    return False
                   
        return True

        
check = Solution()
bills = [5,5,5,10,5,5,10,20,20,20]
print(check.lemonadeChange(bills))
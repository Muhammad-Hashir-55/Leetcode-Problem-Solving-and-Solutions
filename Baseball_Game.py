
class Solution:
    def calPoints(self, operations) -> int:
        new_list = []
        for i in operations:
            if(i =='+'):
                if(len(new_list)>=2):
                    s = new_list[-1] + new_list[-2]
                else:
                    s = new_list[-1]
                new_list.append(s)
            elif(i =='C'):
                new_list.pop()
            elif(i =='D'):
                s = 2*new_list[-1]
                new_list.append(s)
            else:
                new_list.append(int(i))
            print(new_list)
        return sum(new_list)
        
check=  Solution()
print(check.calPoints(["5","-2","4","C","D","9","+","+"]))

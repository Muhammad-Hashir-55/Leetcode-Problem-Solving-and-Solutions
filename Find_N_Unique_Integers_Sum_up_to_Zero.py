class Solution:
    def sumZero(self, n: int) -> List[int]:
        if(n%2 ==0):
            new_list = []
            num = 1
            while(len(new_list)!= n):
                new_list.append(num)
                new_list.append(-num)
                num +=1
            return new_list
        elif(n%2!=0):
            new_list = []
            new_list.append(0)
            num = 1
            while(len(new_list)!= n):
                new_list.append(num)
                new_list.append(-num)
                num +=1
            return new_list

            
        

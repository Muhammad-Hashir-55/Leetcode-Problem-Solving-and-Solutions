class Solution:
    def convertToBase7(self, num: int) -> str:
        c = False
        if(num ==0):
            return "0"
        if(num<0):
            num = abs(num)
            c = True
        s= str(num)
        new_list = []
        while(num):
            mod = num %7
            new_list.append(mod)
            num = num//7
        new_list.reverse()
        new_string = ""
        for i in new_list:
            new_string = new_string + str(i)
        if(c):
            new_string = "-" + new_string
            return new_string
        else:
            return new_string



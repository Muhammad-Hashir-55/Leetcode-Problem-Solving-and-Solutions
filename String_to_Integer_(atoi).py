class Solution:
    def myAtoi(self, s: str) -> int:
        if(s ==''):
            return 0
        
        while(s[0]== " "):
            s = s.replace(" ","",1)
            if(s ==''):
                return 0
        neg = False
        if(s[0]=='-' or s[0]=='+'):
            if(s[0]=='+'):
                s = s.replace(s[0],'',1)
                neg = False
            elif(s[0]=='-'):
                neg = True
                s = s.replace(s[0],'',1)

        nums = '1234567890'
        if(s ==''):
            return 0
        if(s[0].isalpha() or s[0] not in nums):
            return 0
        ss = ""
        for i in s:
            if(i.isdigit()):
                ss +=i
            else:
                break
        print(ss)
        if(neg ==True):
            x= -(int(ss))
            if(x<-2**31):
                return -2**31
            else:
                return x
            

        else:
            x= int(ss)
            if(x >2**31 -1):
                return 2**31 -1
            else:
                return x


        

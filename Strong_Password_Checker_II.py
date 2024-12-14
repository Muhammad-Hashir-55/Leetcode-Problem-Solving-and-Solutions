class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        n = len(password)
        if(n <8):
            return False
        s = 'abcdefghijklmnopqrstuvwxyz'
        ss = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        d = '1234567890'
        sp = "!@#$%^&*()-+"

        c1= False
        c2 = False
        c3 = False
        c4  = False

        for i in s:
            if(i*2 in password):
                return False
            if(i in password):
                c1 = True
        if(c1 == False):
            return False
        for i in ss:
            if(i*2 in password):
                return False
            if(i in password):
                c2 = True
        if(c2 == False):
            return False
        
        for i in d:
            if(i*2 in password):
                return False
            if(i in password):
                c3 = True
        if(c3 == False):
            return False

        for i in sp:
            if(i*2 in password):
                return False
            if(i in password):
                c4 = True
        if(c4 == False):
            return False
        return True
        


        

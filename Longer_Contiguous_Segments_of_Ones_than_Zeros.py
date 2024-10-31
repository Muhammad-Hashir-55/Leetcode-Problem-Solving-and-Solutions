class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        ones = []
        zeros = []
        o = 0
        z = 0
        for i in s:
            if(i =='0'):
                z +=1
                ones.append(o)
                o = 0
            else:
                o +=1
                zeros.append(z)
                z = 0
                
        ones.append(o)
        zeros.append(z)
        
        if(max(ones)<= max(zeros)):
            return False
        else:
            return True

        

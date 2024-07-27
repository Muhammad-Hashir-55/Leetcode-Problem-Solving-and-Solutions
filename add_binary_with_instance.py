result = 0
a = 4
a =str(a)
inta = int(a)

i = len(a) - 1
length_check = len(a)
poww = 0
while(length_check != 0):
    if (a[i] == '1'):
        result = result + (2 **poww)
    poww = poww + 1
    i = i - 1
    length_check = length_check - 1

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        result = 0
        a =str(a)
        i = len(a) - 1
        length_check = len(a)
        poww = 0
        while(length_check != 0):
            if (a[i] == '1'):
                result = result + (2 **poww)
            poww = poww + 1
            i = i - 1
            length_check = length_check - 1
        digi_a  = result
        
        b = str(b)
        result = 0
        i = len(b) - 1
        length_check = len(b)
        poww = 0
        while(length_check != 0):
            if(b[i] == "1"):
                result = result + (2 ** poww)
            poww = poww + 1
            i = i - 1
            length_check= length_check -1
        digi_b = result
        
        final_result = digi_a + digi_b
        binary_result = str(bin(final_result))
        return binary_result[2:]
    

check = Solution()
print(check.addBinary("11" , "1"))


        
class Solution(object):
    def binaryconvertor (a):
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
        return result
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        digit_a = Solution.binaryconvertor(a)
        digit_b= Solution.binaryconvertor(b)
        final_result = digit_a + digit_b
        binary_result = str(bin(final_result))
        return binary_result[2:]
     



check = Solution()
print(check.addBinary("11" , "1"))

        
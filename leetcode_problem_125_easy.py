class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        new_string = ""
        for i in range(len(s)):
            if(s[i].isalnum()):
                new_string = new_string + s[i]
        checking_string = new_string
        reversed_string = ""
        i = len(new_string)
        ii = len(new_string) -1
        while(i >0):
            reversed_string = reversed_string + new_string[ii]
            i = i -1
            ii = ii-1
        print("new_string     ", new_string)
        print("reversed_string", reversed_string)
        if(checking_string == reversed_string):
            return True
        else:
            return False
        
check = Solution()
print(check.isPalindrome("A man, a plan, a canal: Panama"))


        
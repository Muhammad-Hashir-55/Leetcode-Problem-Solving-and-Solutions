class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        i = len(s)
        index = 0
        ii = len(s) -1
        while(index < ii):
            temp = s[index]
            s[index] = s[ii]
            s[ii] = temp
            index = index + 1
            
            i = i - 1
            ii = ii -1
        


check = Solution()
print(check.reverseString(["h","e","l","l","o"])) 
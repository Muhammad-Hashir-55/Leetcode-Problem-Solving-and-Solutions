class Solution(object):
    def halvesAreAlike(self, s):
        """
        :type s: str
        :rtype: bool
        """
        a=  s[:len(s)/2]
        b = s[len(s)/2:]
        vowels = ['a','e','i','o','u','A','E','I','O','U']
        myset = set(vowels)
        av= 0
        bv =0
        for i in a:
            if(i in myset):
                av+=1
        for j in b:
            if(j in myset):
                bv+=1
        if(av == bv):
            return True
        else:
            return False
        

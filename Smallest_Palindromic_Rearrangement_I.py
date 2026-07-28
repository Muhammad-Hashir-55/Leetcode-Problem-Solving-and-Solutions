class Solution:
    def smallestPalindrome(self, s: str) -> str:
        n = len(s)
        if(n %2 == 0):
            half = n//2
            x = s[:half]
            k = sorted(x)
            stri = ('').join(k)
            k = k[::-1]
            stri += ('').join(k)
            return stri
        else:
            half = n//2
            x = s[:half]
            k = sorted(x)
            stri = ('').join(k)
            stri += s[half] 
            k = k[::-1]
            stri += ('').join(k)
            return stri

        
        
        

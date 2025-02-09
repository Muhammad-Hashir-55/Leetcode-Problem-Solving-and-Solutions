class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        count = 0
        res = 0
        n = len(s)
        vowels = {'a','e','i','o','u'}

        for i in range(k):
            if(s[i] in vowels):
                count +=1
        res = count
        for i in range(k,n):
            if(s[i-k] in vowels):
                count -=1
            if(s[i] in vowels):
                count +=1
            res = max(res,count)
        return res

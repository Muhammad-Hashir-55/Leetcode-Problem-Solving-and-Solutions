class Solution:
    def minOperations(self, s: str) -> int:

        if(len(s) ==1):
            return 0
        elif(len(s) == 2):
            k = sorted(s)
            x = ('').join(k)
            if(x == s):
                return 0
            else:
                return -1
    
        k = sorted(s)
        mini = min(k)
        maxi = max(k)
        x = ('').join(k)
        if(x == s):
            return 0
        elif(mini not in s[:-1] and maxi not in s[1:]):
            return 3
        else:
            ans = 0
            if(x[0] != s[0]):
                if(x[-1] != s[-1]):
                    ans +=1
            return ans +1


        

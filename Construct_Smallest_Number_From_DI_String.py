from itertools import permutations
class Solution:
    def smallestNumber(self, pattern: str) -> str:
        numbers = '123456789'
        n = len(pattern)
        req_n = n +1
        arr = list(permutations(numbers,req_n))
        for i in arr:
            found = True
            for j in range(req_n - 1):
                if(pattern[j] == 'I' and i[j] < i[j+1]):
                    continue
                elif(pattern[j] == 'D' and i[j]> i[j+1]):
                    continue
                else:
                    found = False
                    break
            if(found == True):
                return ('').join(i)


        

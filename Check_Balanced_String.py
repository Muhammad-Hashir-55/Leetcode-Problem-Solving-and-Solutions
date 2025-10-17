class Solution:
    def isBalanced(self, num: str) -> bool:
        sumi1 = 0
        sumi2 = 0
        n = len(num)
        for i in range(n):
            if(i % 2 == 0):
                sumi1 += int(num[i])
            else:
                sumi2 += int(num[i])
        return sumi1 == sumi2
        

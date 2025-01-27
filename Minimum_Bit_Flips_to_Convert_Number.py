class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        s1 = bin(start)
        s2 = bin(goal)

        s1  = s1[2:]
        s2 = s2[2:]

        n1 = len(s1)
        n2 = len(s2)

        if(n1>n2):
            while(len(s1)!= len(s2)):
                s2 = '0' + s2
        else:
            while(len(s1)!= len(s2)):
                s1 = '0' + s1


        c =0
        n = len(s1)
        for i in range(n):
            if(s1[i]!= s2[i]):
                c +=1
        return c

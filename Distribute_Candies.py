class Solution:
    def distributeCandies(self, candyType: list[int]) -> int:
        ss = set(candyType)
        n = len(candyType)
        tot = n//2
        now = 0
        coun = 0
        for i in ss:
            coun +=1
            now +=1
            if(now == tot):
                break
        return coun

        

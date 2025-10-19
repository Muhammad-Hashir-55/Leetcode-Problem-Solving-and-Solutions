class Solution:
    def minimumSum(self, num: int) -> int:
        num = str(num)
        k = list(num)
        mini1 = min(k)
        idx1 = k.index(mini1)
        k.pop(idx1)
        mini2 = min(k)
        idx2 = k.index(mini2)
        k.pop(idx2)
        n1 = mini1 + k[0]
        n2 = mini2 + k[1]
        return int(n1) + int(n2)


        

class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        new_string =""
        summ =0
        for i in num:
            summ = summ*10 + i
        summ = summ + k
        l =[]
        while(summ>0):
            mod = summ % 10
            l.append(mod)
            summ = summ //10
        return l[::-1]
        

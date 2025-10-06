class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        m = len(bank)
        n = len(bank[0])
        arr = []
        idx = 0
        for i in bank:
            counting = bank[idx].count('1')
            if(counting):
                arr.append(counting)
            idx +=1
        if(not arr):
            return 0
        if(len(arr) == 1):
            return 0
        else:
            count =0
            prev = arr[0]
            for i in arr[1:]:
                prd = prev * i
                count += prd
                prev = i
            return count





        

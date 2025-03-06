class Solution:
    def addNegabinary(self, arr1: List[int], arr2: List[int]) -> List[int]:
        num1 = 0
        poww = 0
        for i in arr1[::-1]:
            if (i == 1):
                num1 += (-2)**poww
            poww +=1
        
        num2 = 0
        poww = 0
        for i in arr2[::-1]:
            if (i == 1):
                num2 += (-2)**poww
            poww +=1
        tot = num1 + num2
        arr = []

        #math concept
        while(tot != 0):
            x = abs(tot % 2)
            tot  = tot //2
            arr.append(x)
            tot = (-1)* tot
        if(not arr):
            return [0]
        return arr[::-1]

        

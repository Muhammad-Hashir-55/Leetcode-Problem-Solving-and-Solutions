class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        from itertools import permutations
        arr = list(permutations(digits,3))
        print(arr)
        count = 0
        arr = set(arr)
        for i in arr:
            if(i[-1] % 2 == 0 and i[0] != 0):
                count +=1
        return count

        

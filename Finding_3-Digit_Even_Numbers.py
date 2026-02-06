from itertools import permutations
class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        arr  = list(permutations(digits,3))
        a = []
        ss = set()
        for i in arr:
            s = int(str(i[0]) + str(i[1]) + str(i[2]))
            if(s>=100 and (s%2 == 0) and s not in ss):
                a.append(s)
                ss.add(s)
        
        a.sort()
        return a

        

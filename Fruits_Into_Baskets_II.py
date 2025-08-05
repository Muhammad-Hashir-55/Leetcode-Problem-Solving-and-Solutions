class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        coun = 0
        occupied = []
        n = len(fruits)
        for i in range(n):
            c = False
            for j in range(n):
                if(fruits[i] <= baskets[j] and j not in occupied):
                    occupied.append(j)
                    c = True
                    break
                else:
                    continue
            if(c == False):
                coun +=1
        return coun

        

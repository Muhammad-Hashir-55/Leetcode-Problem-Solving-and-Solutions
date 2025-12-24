class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        capacity.sort()
        sumi = sum(apple)
        count = 0
        tot = 0
        for i in capacity[::-1]:
            tot += i
            count +=1
            if(tot >= sumi):
                break
        return count
        

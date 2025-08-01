class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n= len(boxes)
        arr = []
        for i in range(n):
            tot = 0
            for j in range(n):
                if(i == j):
                    continue
                if(boxes[j] == '0'):
                    continue
                else:
                    tot += abs(i -j)
            arr.append(tot)
        return arr
            
        

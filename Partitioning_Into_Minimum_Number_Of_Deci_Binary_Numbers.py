class Solution:
    def minPartitions(self, n: str) -> int:
        arr = []
        for i in n:
            arr.append(int(i))
        return max(arr)
        

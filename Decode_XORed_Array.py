class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        arr = []
        arr.append(first)
        for i in encoded:
            arr.append(first ^ i)
            first = arr[-1]
        return arr
        

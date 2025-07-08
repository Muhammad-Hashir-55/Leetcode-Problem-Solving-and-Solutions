class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        n = len(changed)
        arr = []
        if(n % 2 != 0):
            return []
        count = Counter(changed)
        changed.sort()

        for i in changed:
            if(count[i] == 0):
                continue
            if(count[2*i] == 0):
                return []
            arr.append(i)
            count[i] -=1
            count[2*i] -=1
        return arr
            
        

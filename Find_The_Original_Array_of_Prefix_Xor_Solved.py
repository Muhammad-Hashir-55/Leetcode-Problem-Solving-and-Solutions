class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        arr = [pref[0]]
        n = len(pref)
        for i in range(1,n):
            x = pref[i] ^ pref[i-1]
            arr.append(x)
        return arr
        

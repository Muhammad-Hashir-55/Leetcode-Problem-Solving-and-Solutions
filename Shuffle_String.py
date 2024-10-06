class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        new_string = ""
        l1 = list(s)
        ii=  0
        for i in indices:
            l1[i] = s[ii]
            ii +=1
        for j in l1:
            new_string = new_string + j
        return new_string

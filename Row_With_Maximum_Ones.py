class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        maxi = -1
        n = len(mat)
        arr = []
        for i in mat:
            maxi = max(maxi,i.count(1))
        
        for i in range(n):
            if(mat[i].count(1)==maxi):
                arr.append(i)
                break
        arr.append(maxi)
        return arr

        

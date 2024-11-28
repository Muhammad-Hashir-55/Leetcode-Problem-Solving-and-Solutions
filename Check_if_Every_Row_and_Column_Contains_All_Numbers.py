class Solution:
    def checkValid(self, matrix) -> bool:
        nums = []
        for i in matrix:
            for j in i:
                if(j not in nums):
                    nums.append(j)
        n= len(matrix)
        ii = 0
        if(len(nums)!= n):
            return False

        for i in nums:
            for j in matrix:
                if(i not in j):
                    return False
        other = []
        n = len(matrix)
        for i in range(n):
            row = []
            for j in range(n):
                row.append(matrix[j][i])
            other.append(row)

        n= len(other)
        ii = 0

        for i in nums:
            for j in other:
                if(i not in j):
                    return False
        return True

class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        maxi = 0
        n = len(dimensions)
        for i in dimensions:
            d_l = (i[0]**2 + i[1]**2)**0.5
            if(maxi < d_l):
                maxi = d_l
        maxi_a = 0
        
        for i in dimensions:
            d_l = (i[0]**2 + i[1]**2)**0.5
            a = i[0] * i[1]
            if(maxi == d_l):
                if(maxi_a < a):
                    maxi_a = a
        return maxi_a
        
        

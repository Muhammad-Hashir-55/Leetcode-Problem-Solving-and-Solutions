class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort()
        maxi = 0
        n = len(points)
        for i in range(n-1):
            if(abs(points[i][0] - points[i+1][0]) > maxi):
                maxi = abs(points[i][0] - points[i+1][0])
        return maxi
        

class Solution(object):
    def checkStraightLine(self, coordinates):
        """
        :type coordinates: List[List[int]]
        :rtype: bool
        """
        x0,y0 = coordinates[0]
        x1,y1 = coordinates[1]
        for i in range(2,len(coordinates)):
            xi,yi = coordinates[i]
            if((y1-y0)*(xi-x0) != (yi-y0)*(x1-x0)):
                return False
        return True
        

class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        xx =bin(x)
        xx = xx[2:]
        yy = bin(y)
        yy = yy[2:]
        if(len(xx)>len(yy)):
            while(len(yy)!= len(xx)):
                yy = '0'+yy
            diff = 0
            for i in range(len(xx)):
                if(xx[i] != yy[i]):
                    diff +=1
            return diff
        else:
            while(len(xx)!= len(yy)):
                xx = '0' + xx
            diff = 0
            for i in range(len(yy)):
                if(yy[i]!= xx[i]):
                    diff +=1
            return diff


        

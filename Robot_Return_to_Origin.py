class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        saved = [0,0]
        starting = [0,0]
        for i in moves:
            if(i == "L"):
                starting[0] = starting[0] - 1
            elif(i == "R"):
                starting[0] = starting[0] +1
            elif(i == "U"):
                starting[1] = starting[1] + 1
            else:
                starting[1] = starting[1] -1
        if(starting == saved):
            return True
        else:
            return False
        

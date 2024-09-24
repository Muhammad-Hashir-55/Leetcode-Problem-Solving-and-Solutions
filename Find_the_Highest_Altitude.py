class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        new_list =[]
        att = 0
        new_list.append(att)
        for i in gain:
            att = att + i
            new_list.append(att)
        return max(new_list)
        

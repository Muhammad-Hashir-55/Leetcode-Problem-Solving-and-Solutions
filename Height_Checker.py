class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        indices = 0
        expected = sorted(heights)
        for i in range(len(heights)):
            if(heights[i]!= expected[i]):
                indices = indices +1
        return indices

        
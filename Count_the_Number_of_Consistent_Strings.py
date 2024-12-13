class Solution(object):
    def countConsistentStrings(self, allowed, words):
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        """
        n = len(words)
        c = 0
        for i in range(n):
            dontadd = False
            for j in words[i]:
                if(j in allowed):
                    continue
                else:
                    dontadd = True
                    break
            if(dontadd == False):
                c +=1
        return c



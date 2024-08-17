class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        collection = 0
        for i in jewels:
            if(i in stones):
                if(stones.count(i)>1):
                    collection = collection + stones.count(i)
                else:
                    collection = collection +1
        return collection 
            
        
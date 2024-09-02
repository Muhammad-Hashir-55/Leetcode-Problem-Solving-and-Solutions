class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        for i in sentence:
            if(i in alphabets):
                alphabets.remove(i)
        if(alphabets == []):
            return True
        else:
            return False
        

class Solution(object):
    def reversePrefix(self, word, ch):
        """
        :type word: str
        :type ch: str
        :rtype: str
        """
        if(ch not in word):
            return word
        new_string = word[:word.index(ch)+1]
        reversed_string = ""
        i = len(new_string)-1
        ii = len(new_string)
        while(ii != 0):
            reversed_string = reversed_string + new_string[i]
            i -=1
            ii -=1
        return reversed_string + word[word.index(ch) +1:]

        

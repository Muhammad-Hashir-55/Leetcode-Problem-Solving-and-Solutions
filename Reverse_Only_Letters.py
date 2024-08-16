class Solution(object):
    def reverseOnlyLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        index = 0
        i = len(s) -1
        new_list = []
        for j in s:
            new_list.append(j)
        while(index<i):
            if(not new_list[index].isalpha()):
                index = index+1
                continue
            if(not new_list[i].isalpha()):
                i = i -1
                continue
            else:
                new_list[index],new_list[i] = new_list[i],new_list[index]
                index = index+1
                i = i -1
        new_string = ""
        for k in new_list:
            new_string = new_string + k
        return new_string
        
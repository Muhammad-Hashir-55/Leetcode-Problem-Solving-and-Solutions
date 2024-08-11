class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = ["a","e","i","o","u","A","E","I","O","U"]
        new_list = []
        for i in s:
            new_list.append(i)
        index = 0
        i = len(new_list) -1
        while(index<i):
            if(new_list[index] not in vowels):
                index = index +1
                continue
            if(new_list[i] not in vowels):
                i=  i -1
                continue
            temp = new_list[index]
            new_list[index]= new_list[i]
            new_list[i] = temp
            index = index +1
            i = i -1
        new_string = ""
        for j in new_list:
            new_string = new_string + j
        s = new_string
        return s
        
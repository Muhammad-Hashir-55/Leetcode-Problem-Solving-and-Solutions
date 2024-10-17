class Solution:
    def reverseWords(self, s: str) -> str:
        ss = s.split(" ")
        while('' in ss):
            ss.remove('')
        new_string = ""
        for i in ss[::-1]:
            new_string = new_string + i
            new_string = new_string + " "
        new_string = new_string[:-1]
        return new_string
        
        

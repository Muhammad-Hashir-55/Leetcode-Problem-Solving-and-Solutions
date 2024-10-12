class Solution:
    def freqAlphabets(self, s: str) -> str:
        new_string = ""
        my_dict = {'1':'a','2':'b','3':'c','4':'d','5':'e','6':'f','7':'g','8':'h','9':'i','10#':'j','11#':'k','12#':'l','13#':'m','14#':'n','15#':'o','16#':'p','17#':'q','18#':'r','19#':'s','20#':'t','21#':'u','22#':'v','23#':'w','24#':'x','25#':'y','26#':'z'}
        if('#'not in s):
            for i in s:
                new_string = new_string + my_dict[i]
            return new_string
        else:
            new_string = ""
            i = len(s)-1
            while(i>-1):
                if(s[i]== '#'):
                    new_s = ""
                    new_s = s[i]+s[i-1]+s[i-2]
                    new_s = new_s[::-1]
                    new_string = new_string + my_dict[new_s]
                    i -=2
                    
                else:
                    new_string = new_string + my_dict[s[i]]
                i = i-1
            return new_string[::-1]

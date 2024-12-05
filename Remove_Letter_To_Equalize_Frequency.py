class Solution:
    def equalFrequency(self, word: str) -> bool:
        n = len(word)

        for i in range(n):
            x = word[:i] + word[i+1:]
            my_dict = {}
            for j in x:
                if(j not in my_dict):
                    my_dict[j] =1
                else:
                    my_dict[j] +=1
            arr = []
            for k in my_dict.values():
                arr.append(k)
            if(len(set(arr)) ==1):
                return True
        return False
        

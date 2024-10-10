class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        s1 = "qwertyuiop"
        s2 = "asdfghjkl"
        s3 = "zxcvbnm"
        c1 = False
        c2 = False
        c3 = False

        new_list  =[]
        for i in words:
            c1 = False
            c2 = False
            c3 = False
            original = i.lower()
            if(original[0] in s1):
                for j in original:
                    if(j not in s1):
                        c1 = True
                        break
                
            elif(original[0] in s2):
                for j in original:
                    if(j not in s2):
                        c2 = True
                        break
            elif(original[0] in s3):
                for j in original:
                    if(j not in s3):
                        c3 = True
                        break
            if(c1==False and c2 == False and c3 == False):
                new_list.append(i)
        return new_list

        

class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        my_dict = {'a':'0','b':'1','c':'2','d':'3','e':'4','f':'5','g':'6','h':'7','i':'8','j':'9'}
        s1 = ""
        s2 = ""
        tg = ""
        for i in firstWord:
            s1 += my_dict[i]
        for j in secondWord:
            s2 += my_dict[j]
        for k in targetWord:
            tg += my_dict[k]
        if(int(tg)==int(s1)+int(s2)):
            return True
        else:
            return False

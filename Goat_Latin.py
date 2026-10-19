class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        arr = []
        sentence = sentence.split(' ')
        a_s = 2
        for i in sentence:
            x = i
            st = x[0]
            if(st.lower() not in 'aeiou'):
                x = x[1:]
                x += st
            x +='m' + (a_s *'a')
            a_s +=1
            arr.append(x)
        return (' ').join(arr)
        
        

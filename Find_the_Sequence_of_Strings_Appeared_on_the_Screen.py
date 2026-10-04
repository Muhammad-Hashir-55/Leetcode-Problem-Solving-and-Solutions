class Solution:
    def stringSequence(self, target: str) -> List[str]:
        alphas = 'abcdefghijklmnopqrstuvwxyz'
        n = 26
        s = 'a'
        arr = ['a']
        idx = 0
        while(s != target):
            
            if(s[idx] == target[idx]):
                s +='a'
                idx +=1
                arr.append(s)
                continue
            x = s[idx]
            i = alphas.index(x)
            i = (i+1)%n
            s = s[:idx]
            s += alphas[i]
            arr.append(s)
        return arr
        

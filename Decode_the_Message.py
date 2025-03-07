class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        s = 'abcdefghijklmnopqrstuvwxyz'
        key = key.split(' ')
        sss = ''
        for i in key:
            sss += i
        
        print(key)
        dic = {}
        n = len(set(sss))
        dic1 = {}

        ssss = ''
    
        for i in sss:
            if(i in dic1):
                dic1[i] +=1
            else:
                dic1[i] = 1
        for i in dic1:
            ssss += i
    
        
        for i in range(n):
            dic[ssss[i]] = s[i]
        
        ss = ''
        for i in message:
            if(i in dic):
                ss += dic[i]
            else:
                ss += i
        return ss
        

class Solution:
    def greatestLetter(self, s: str) -> str:
        ss = 'abcdefghijklmnopqrstuvwxyz'
        arr = []
        for i in ss:
            if(i in s and i.upper() in s):
                arr.append(i.upper())
        if( not arr):
            return ''
        k = sorted(arr)
        return k[-1]
            
        

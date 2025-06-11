class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        small_n = len(p)
        n = len(s)
        if(small_n > n):
            return []

        k = sorted(p)
        p = ''.join(k)
    
        arr = []
        win = ''
        start  =0
        
        for i in s:
            win += i
            if(len(win) == small_n):
                if(p == ''.join(sorted(win))):
                    arr.append(start)
                win = win[1:]
                start +=1

        return arr


            
                


        
